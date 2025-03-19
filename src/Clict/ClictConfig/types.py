from dataclasses import field
from pathlib import Path
from subprocess import getoutput
from enum import IntFlag


from enum import Enum,IntFlag

class CfgType(IntFlag):
	none	 = 0
	config   = 2**1
	root     = 2**2
	folder   = 2**3
	file     = 2**4
	section  = 2**5
	key      = 2**6
	val      = 2**7



class OptFlag(IntFlag):
		strip_file_Prefix   = 1
		strip_file_Suffix   = 2
		strip_folder_Prefix = 4
		strip_folder_Suffix = 8
		split_on_Underscore = 16
		split_on_dot        = 32
		split_on_dash       = 64


class ConfSelf(clictbase):
	def __init__(__s,*a,**k):
		__s._self=k.get('node')
		__s.root=k.get('root')
		__s.name= k.get('name')
		__s.opts=k.get('opts',ConfOpts())
		__s.parent=k.get('parent')
		__s.path=Path(k.pop('path',''))
		__s.file=k.get('file')
		__s.section=k.get('section')
		__s.key=k.get('key')
		__s.value=k.get('value')
		__s.strvalue=str(repr(__s.value))
		__s.stat=Stat(path=__s.path,**k)
		__s.types=CfgType(0)
		__s.type=CfgType(0)
		__s.parser=k.get('parser')
		__s.interpolation=None
		__s.__types__()
		if __s.name is None:
			if __s.opts.flags.strip_file_Suffix:
				for suffix in __s.opts.include.file.suffix:
					__s.name =__s.path.name.removesuffix(suffix)

	def __types__(__s):
		T=CfgType
		S=__s.stat
		__s.types=(T.folder*S.folder)+(T.file*S.file)+(T.section*S.section)+(T.key*S.key)+(T.val*S.value)
	def self(__s):
		return __s._self


class ConfOpts(Opts):
	def __init__(__s,**opts):
		super().__init__()
		__s.exclude.file.prefix = ['.', '_']
		__s.exclude.file.suffix = ['.bak', '.old', '.disabled']
		__s.exclude.folder.prefix = ['.', '_']
		__s.include.file.suffix = ['.conf', '.config', '.init', '.ini', '.cfg', '.toml', '.profile','.service','.unit','.desktop','']
		__s.parser.delimiters=(':', '=')
		__s.parser.allow_no_value=True
		__s.parser.strict=False
		__s.parser.opts = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}
		__s.flags=OptFlag(0)


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
