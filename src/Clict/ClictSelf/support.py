from Clict.ClictBase.base  import Clict as clictbase
from enum import Enum,StrEnum
from dataclasses import dataclass,field
from collections import namedtuple
import re





@dataclass()
class RGB(namedtuple('RGB', ['r', 'g', 'b', 'l', 'd'])):
	r: int = field(default=0)
	g: int = field(default=0)
	b: int = field(default=0)
	l: int = field(default=38)  # 38=foreground, 48=background
	d: int = field(default=2)   # 2=24bit, 5=8bit, 1=bold

	def __new__(cls, r=None ,g=None ,b=None ,l=None ,d=None):
		args={	'r':r or 0,	'g':g or 0,	'b':b or 0,	'l':l or 38, 'd':d or 2	}
		return super().__new__(cls, *args.values())

	def __str__(s):
		return '{ESC}[{L};{D};{R};{G};{B}m'.format(ESC='\x1b',L=s.l,D=s.d,R=s.r,G=s.g,B=s.b)


class ColorSet(clictbase):
	CLRTREE  : str=field(default_factory=RGB)
	CLRKEY   : str=field(default_factory=RGB)
	CLRSEP   : str=field(default_factory=RGB)
	CLRVAL   : str=field(default_factory=RGB)
	CLRTIT   : str=field(default_factory=RGB)
	CLRCALL  : str=field(default_factory=RGB)
	CLRALGN  : str=field(default_factory=RGB)
	CLRRST   : str=field(default='\x1b[m')
	def __init__(s,TREE='',KEY='',SEP='',VAL='',CALL='',ALGN='',TIT=''):
		kwlist=  ['TREE', 'KEY', 'SEP', 'VAL', 'CALL', 'ALGN', 'TIT']
		arlist=[   TREE ,  KEY ,  SEP ,  VAL  ,  CALL , ALGN ,  TIT ]
		def dumbkeywoardwrapper(**k):
			{setattr(s,*(f'CLR{item}',k.get(item))) for item in kwlist}
			if k.get('CLRTIT') == '' :
				s.CLRTIT=s.CLRKEY
			s.CLRRST='\x1b[m'
			if all([(True*(getattr(s,f'CLR{attr}')=='')) for attr in kwlist]):
				s.CLRRST=''
		dumbkeywoardwrapper(**{key:val for key,val in zip( kwlist,arlist)})

DefaultColorTemplate={
	'CLRTREE': '{CLRTREE}',
	'CLRKEY' : '{CLRKEY}',
	'CLRSEP' : '{CLRSEP}',
	'CLRVAL' : '{CLRVAL}',
	'CLRCALL': '{CLRCALL}',
	'CLRRST' : '{CLRRST}',
	'CLRTIT' : "{CLRTIT}",
}
DefaultColorset=ColorSet(
	RGB(96,  96, 96),
	RGB(128,192,255),
	RGB(255,255,255),
	RGB(255,255, 96),
)



class Prop(clictbase):
	def __init__(s,*a,**k):
		s.str.color = True
		s.str.tree = False
		s.repr.color = True
		s.repr.tree = True
		super().__init__(*a, **k)

class Opts(clictbase):
	def __init__(s,*a,**k):
		s._self=k.get('self')
		s.repr.colors.tree.rgb = DefaultColorset
		s.repr.colors.tree.bw = ColorSet()
		s.repr.colors.tree.tpl = DefaultColorTemplate
		s.repr.symbols.tree.lastnode = '┗━━━┳━╼'
		s.repr.symbols.tree.clictnode = '┣━━━┳━╼ '
		s.repr.symbols.tree.parent = '┃'
		s.repr.symbols.tree.replace = '┳', '━'
		s.repr.symbols.tree.allign = ' '


