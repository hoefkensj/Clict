from dataclasses import field
from pathlib import Path
from subprocess import getoutput
from enum import IntFlag

from Clict.base.Clict import Clict as clictbase
from Clict.base.self import Opts


class Stat:
	def __init__(__s,path):
		__s.path=path
		real=None
		virt=None
		real=Path(path).expanduser().resolve()
		if '##' in str(real):
			real,virt=str(path.absolute()).split('##')
			real=Path(real)
			virt=Path(virt)
		__s.exists  = real.exists()
		__s.file    = real.is_file()
		__s.folder  = real.is_dir()
		__s.symlink = real.is_symlink()
		__s.ftype   = getoutput(f'file {real}').split(':')[-1].split()
		__s.virtual = False
		__s.section = False
		__s.key     = False
		__s.value   = False
		__s.object  = False
		if virt is not None:
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
		from pathlib import Path
		__s.name= k.get('name')
		__s.opts=k.get('opts',ConfOpts())
		__s.parent=k.get('parent')
		__s.path=Path(k.get('path'))
		__s.file=k.get('file')
		__s.section=k.get('section')
		__s.key=k.get('key')
		__s.stat=Stat(path=__s.path)
		__s.types=None
		__s.type=None
		__s.parser=k.get('parser')
		__s.interpolation=None

		if __s.name is None:
			if __s.opts.flags.strip_file_Suffix:
				for suffix in __s.opts.include.file.suffix:
					__s.name =__s.path.name.removesuffix(suffix)
		__s.__types__()
	def __types__(__s):
		t=[]
		t+= ['folder' ]*__s.stat.folder
		t+= ['file' ]*__s.stat.file
		t+= ['section' ]*__s.stat.section
		t+= ['key' ]*__s.stat.key

class ValueSelf(clictbase):
	def __init__(__s,*a,**k):
		__s.name= k.get('name')
		__s.parent=k.get('parent')
		__s.path=Path(k.get('path'))
		__s.file=k.get('file')
		__s.section=k.get('section')
		__s.key=k.get('key')
		__s.originalvalue=k.get('value')
		__s.strvalue=str(k.get('value'))


class ConfOpts(Opts):
	def __init__(__s,**opts):
		super().__init__()
		__s.exclude.file.prefix = ['.', '_']
		__s.exclude.file.suffix = ['.bak', '.old', '.disabled']
		__s.exclude.folder.prefix = ['.', '_']
		__s.include.file.suffix = ['.conf', '.config', '.init', '.ini', '.cfg', '.toml', '.profile','service','unit','']
		__s.parser.delimiters=(':', '=')
		__s.parser.allow_no_value=True
		__s.parser.strict=False
		__s.parser.opts = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}
		__s.flags=OptFlag(15)


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
