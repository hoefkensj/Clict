
#!/usr/bin/env python
import os
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation
from Clict.Typedef import Clict

def getFileType(c):
	ext=c._self.opts.suffix
	def isconfig(): return bool(c._path.suffix.casefold() in ext)
	def isdisabled(p): return bool(p.name.startswith('_') or p.suffix in ['.old','.bak','.not'])
	r=Clict()
	r.file=bool(c._path.is_file())
	r.folder=bool(c._path.is_dir())
	r.config=isconfig()
	r.disabled=isdisabled(c._path)
	return r

def makeUnique(c,Name):
	def incSuffix(name):
		if '#' in name:
			parts=name.split('#')
			if parts[-1].isnumeric():
				name='#'.join([*[parts[:-1],str(int(parts[-1])+1)]])
		else:
			name+='#1'
		return name
	FUSE=1
	name=Name.stem
	while name in c:
			if name != Name.name and FUSE:
				name=Name.name
				FUSE=0
				continue
			name=Name.stem
			name=incSuffix(name)
	return name

def newConfig():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(),
										 delimiters=':',
										 allow_no_value=True)  # create empty config
	cfg.optionxform = lambda option: option
	return cfg

class from_Config(Clict):
	__module__ = None
	__qualname__ = "Clict"
	__version__ = 1
	def __init__(__s,p,cat=None,parent=None,**opts):
		__s._path=Path(p)
		__s._name=__s._path.stem
		__s._parent= parent or None
		__s._cat=cat or []
		for item in opts:
			if item in __s._optb:
				__s._optb[item]=bool(opts.get(item))
		__s._self=__s.__self__()
		__s._type=getFileType(__s)



		__s.__read__()

	def __self__(__s):
		self=Clict()
		self.name=__s._name
		self.path=__s._path
		self.file=__s._type.file
		self.folder=__s._type.folder
		self.config=__s._type.config
		parent=__s.get('_parent')
		if parent:
			self.parent=parent.get('_name')
		self.flag.strip.filesuffix = True
		self.flag.strip.fileprefix = True
		self.flag.strip.folderprefix = True
		self.flag.strip.foldersuffix = True
		self.flag.split.on_underscore = True
		self.flag.ignore_dotfiles = True
		self.opts.suffix= ['.conf','.config','.init', '.ini', '.cfg','.toml','.unit','.service','.profile']
		return self

	def __read__(__s):
		if not __s._type.disabled:
			if __s._type.folder:
				for item in [*__s._path.glob('*')]:
					cat=[*__s._cat,__s._name]
					__s[makeUnique(__s,item)]=from_Config(item,cat=cat ,parent=__s)
			else:
				cfg=None
				if __s._type.config:
					try:
						cfg = newConfig()
						cfg.read(__s._self.path)
					except Exception as E:
						cfg={'error': E}
				else:
					try:
						cfg = newConfig()
						cfg.read(__s._path)
					except Exception as E:
						cfg=None

				if cfg is not None:
					for section in cfg:
						if section == 'DEFAULT':
							continue
						for key in cfg[section]:
							if key in cfg['DEFAULT']:
								if cfg['DEFAULT'][key] == cfg[section][key]:
									continue
							__s[section][key] = cfg[section][key]


# if '-' in section:
# 	for key in cfg[section]:
# 		if key in cfg['DEFAULT']:
# 			if cfg['DEFAULT'][key] == cfg[section][key]:
# 				continue
#							__s[section.split('-')[0]]['-'.join(section.split('-')[1:]).replace('-', '.')][key]= cfg[section][key]

# 		O=lambda x :__s._optb.get(x)
#
#
# if item.stem.startswith('.'):
# 	if O('ignore_dotfiles'):
# 		continue
# if O('strip_folderext') else str(item)
# and O('strip_folderprefix'):
#
# and O('strip_folderprefix'):
#
