
#!/usr/bin/env python
import os
import termios
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser
from Clict.Typedef import ClictSelf as Clict
from contextlib import suppress
def getFileType(c):
	p=c._self._get('path')

	exc=c._opts.suffix_exclude
	inc=c._opts.suffix_include
	isconfig= lambda t: t.casefold() in inc
	isexclude= lambda t: t.casefold() in exc
	isdisabled= lambda n: n.startswith('_')
	iscustom=lambda t :  t.casefold() not in[*inc,*exc]
	r=Clict()
	r.exists=p.exists()
	r.file=p.is_file()
	r.folder=p.is_dir()
	r.config=isconfig(t=p.suffix)
	r.ignore=isexclude(t=p.suffix)
	r.disable=isdisabled(p.name)
	return r






def readConfig(file):
	def testconfig(c):
		result=False
		with suppress(Exception):
			for section in c:
				for key in c[section]:
						test=c[section][key]
				return True
		return result

	opts={'delimiters':(':', '='), 'allow_no_value':True}
	CEI = lambda : ConfigParser(interpolation=ExtendedInterpolation(),**opts,strict=False)
	CBI = lambda : ConfigParser(interpolation=BasicInterpolation(),**opts)
	CNI = lambda : ConfigParser(interpolation=None,**opts)
	CRP = lambda : RawConfigParser(**opts,strict=False)

	cfg=None
	i=0
	while i<4:
		cfg = [CEI,CBI,CNI,CRP][i]()
		parser=['extended','basic','none','raw'][i]
		cfg.optionxform = lambda option: option
		cfg.read(file)
		if testconfig(cfg):
			result=[CEI,CBI,CNI,CRP][i]()
			result.optionxform = lambda option: option
			result.read(file)
			break
		else:
			i+=1

	return cfg

class from_Config(Clict):
	__module__ = None
	__qualname__ = "Clict"
	__version__ ='0.5.04'
	def __init__(__s,*a,**k):
		__s.__args__(*a)
		__s.__kwargs__(**k)
		__s.__read__()

	def __kwargs__(__s,**k):
		self=k.pop('self',{})
		opts=k.pop('opts',{})
		__s.__self__(**self)
		__s.__opts__(**opts)
	def __args__(__s,*a):
		for path in a[::-1]:
			__s._self.path=path
			__s.__self__()

	def __self__(__s,**self):
		path=self.pop('p',self.pop('path',__s._self.path))
		cat=self.pop('c',self.pop('cat',[]))
		parent=self.pop('P',self.pop('parent',None))
		name=self.pop('n',self.pop('name','root'))
		path=Path(path).expanduser().resolve().absolute()
		__s._self.path=path
		__s._self.parent= lambda : parent
		__s._self.name=path.name
		__s._self.stem=path.stem
		__s._self.suffix=path.suffix[1:]
		__s._self.cat=cat
		__s.__type__()

	def __type__(__s):

		t=getFileType(__s)
		__s._self.type.file=t.file
		__s._self.type.exists=t.exists
		__s._self.type.folder=t.folder
		__s._self.type.config=t.config
		__s._self.type.ignore=t.ignore
		__s._self.type.disable=t.disable

	def __opts__(__s,**opts):
		__s._opts.strip_fileSuffix = True
		__s._opts.strip_filePrefix = True
		__s._opts.strip_folderPrefix = True
		__s._opts.strip_folderSuffix = True
		__s._opts.split_onUnderscore = True
		__s._opts.include_dotFiles = False
		__s._opts.include_dotFolders = False
		__s._opts.suffix_include= ['.conf','.config','.init', '.ini', '.cfg','.toml','.profile']
		__s._opts.suffix_exclude= ['.bak','.old','.disabled','.toml']

	def __read__(__s):
		if __s._self.type.get('folder'):
			__s.__folder__()

		elif __s._self.type.get('file'):
				c=Clict()

				cfg=readConfig(__s._self.path)
				for section in cfg:
					if section == 'DEFAULT':
						continue
					for key in cfg[section]:
						if key in cfg['DEFAULT']:
							if cfg['DEFAULT'][key] == cfg[section][key]:
								continue
						c[section][key] = cfg[section][key]


					if len(c[section])==0:
						c[section]=str(None)
				if len(c)==0:
					c=str(None)
				else:
					for section in c:
						for key in c[section]:
							__s[section][key]=c[section][key]

		else:
			__s.error=f'{__s._self.get("path")} : exists = {__s._self.type.exists}'
			# print(, 'is not a config',__s.error)




	def __folder__(__s):
		itemlist = [*__s._self.path.glob('*')]
		for item in [*__s._self.path.glob('*')]:
			itemlist.remove(item)
			cat = [*__s._self.cat, __s._self.name]
			s = Clict()
			if item.suffix not in __s._opts.suffix_exclude:
				s.p = item
				s.P = __s
				s.name = item.name
				s.suffix = item.suffix[1:]
				s.stem = item.stem
				s.cat = cat
				name = s.stem.replace('.', '_')
				if item.suffix in __s._opts.suffix_include:
					__s[name] = from_Config(self=s, opts=__s._opts)
				elif len(item.suffix) != 0:
					__s[item.suffix[1:]][name]=from_Config(self=s, opts=__s._opts)
				else:
					__s[name] = from_Config(self=s, opts=__s._opts)


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
