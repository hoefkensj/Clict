from Clict.types.base  import Clict as clictbase
from dataclasses import dataclass,field

class Opts(clictbase):
	def __init__(s,*a,**k):
		s.str.color=True
		s.str.tree=False
		s.repr.color=True
		s.repr.tree=True
		s.colors.tree.rgb={
			'CLRTREE':'\x1b[38;2;96;96;96m',
			'CLRKEY':'\x1b[1;38;2;128;192;255m',
			'CLRVAL':'\x1b[3;38;2;255;255;96m',
			'CLRCALL':'\x1b[3;38;2;255;32;32m',
			'CLRRESET':'\x1b[m'
		}
		s.colors.tree.tpl={
			'CLRKEY'   : '{CLRKEY}',
			'CLRVAL'   : '{CLRVAL}',
			'CLRTREE'  : '{CLRTREE}',
			'CLRCALL'  : '{CLRCALL}',
			'CLRRESET' : '{CLRRESET}',
		}

class Self(clictbase):
	def __init__(__s,*a,**k):
		__s.name= k.get('name')
		__s.opts=Opts(k.get('opts'))
		__s.parent=k.get('parent')

class ConfSelf(clictbase):
	def __init__(__s,*a,**k):
		from pathlib import Path
		__s.name= k.get('name')
		__s.opts=Opts(k.get('opts'))
		__s.parent=k.get('parent')
		__s.path=Path(k.get('path'))
		__s.stat=k.get('stat')
		__s.parser.delimiters=(':', '=')
		__s.parser.allow_no_value=True
		__s.parser.strict=False
		if __s.name==None:
			 __s.name=__s.path.name


class ConfOpts(Opts):
	def __init__(__s):
		super().__init__()
		__s.exclude.file.prefix = ['.', '_']
		__s.exclude.file.suffix = ['.bak', '.old', '.disabled']
		__s.exclude.folder.prefix = ['.', '_']
		__s.include.file.suffix = ['.conf', '.config', '.init', '.ini', '.cfg', '.toml', '.profile']
		__s.parser = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}



	# path:Path=field(default=None)
	# name:str=field(default='')
	# type:str=field(default='virtual')
	#
	# cat:list[str]=field(default=None)
	# opts:Clict=field(default_factory=Clict)
	# stat:Stat=field(default_factory=lambda:None)

	# @property
	# def parent(s):
	# 	return s._parent
	# @parent.setter
	# def parent(s,parent):
	# 	s._parent=lambda : parent

	# def __post_init__(__s):
		# if __s.path is not None:
		# 	__s.stat = Stat(__s.path)
		# 	if __s.stat.exists:
		# 		__s.type = __s.stat.ftype if __s.stat.file else 'folder'
		# 	else:
		# 		__s.type = 'virtual'
		# 		__s.path = Path('virtual://', *Path(__s.path).parts)
		# 	__s.name = __s.path.name
		# 	__s.parent = Path(__s.path.parent)
		# 	__s.cat = [*Path(__s.path.parent).parts]
		# elif __s.name is not None:
		# 	__s.type = 'virtual'
		# 	if __s.parent is not None:
		# 		__s.path = Path('virtual://', *__s.parent()._self.cat, __s.parent()._self.name, __s.name)
		#
		# 	else:
		# 		__s.path = Path('virtual://', __s.path)
		# __s.stat = Stat(__s.path)
		#

