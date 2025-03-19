from Clict.ClictBase.clict import Clict as clictbase
from dataclasses import dataclass,field
from pathlib import Path
@dataclass
class Stat:
	_self:clictbase
	_path:Path=field(default=Path())
	root:bool=field(default=False)
	real:bool=field(default=False)
	imag:bool=field(default=False)
	exists:bool=field(default=False)
	virtual:bool=field(default=False)
	symlink:bool=field(default=False)
	file:bool=field(default=False)
	folder:bool=field(default=False)
	section:bool=field(default=False)
	key:bool=field(default=False)
	value:bool=field(default=False)

	def __init__(s,**k):
		s._self=k.get('obj')
		s._path=k.get('path')
			__s.virtual=True
			__s.section=True
			__s.key=False
			section=virt
			if '::' in str(virt):
				__s.section = False
				__s.value = True
			elif '$$' in str(virt):
				section,key=str(virt).split('$$')
				__s.section=False
				__s.key=True

				realNone
		virt=None
		real=Path(path).expanduser().resolve()
		isroot=k.get('isroot',False)
		if '##' in str(real):
			real,virt=str(path.absolute()).split('##')
			real=Path(real)
			virt=Path(virt)