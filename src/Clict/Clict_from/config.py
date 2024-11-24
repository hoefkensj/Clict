
#!/usr/bin/env python
import os
import sys
import termios
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser
from Clict.Clict import Clict
from contextlib import suppress
from Clict.structs import self






def CheckFile(__s):
	def isCfg():
		config=False
		if __s._self.path.is_file():
				opts = {
					'delimiters': (':', '='),
					'allow_no_value': True
					}
				tmp=RawConfigParser(**opts, strict=False)
				config=True
				try:
					tmp.read(__s._self.path)
				except Exception:
					config=False
		return config
		
		
	isexclude= lambda t: t.casefold() in __s._opts.exclude.file.prefix
	isdisabled= lambda n: n.startswith('_')
	p = __s._self._get('path')
	r=Clict()
	r.config=isCfg()
	r.ignore=isexclude(t=p.suffix)
	r.disable=isdisabled(p.name)

	this=Clict()
	this.exists = p.exists()
	this.file   = p.is_file()
	this.folder = p.is_dir()
	this.config = r.config
	this.ignore = r.ignore
	this.disable = r.disable
	__s._self.type=this
	
def readConfig(file):
	result=False

	def read(i):
		a = ConfigParser(interpolation=intr[i](), **opts)
		a.optionxform = lambda option: option
		try:
			result = Clict()
			a.read(file)
			cfg=a
			for sec in cfg:
				for key in cfg[sec]:
					result[sec][key]=cfg[sec][key]
		except Exception as E:
			result=read(i+1)
		return result
		
	no=lambda :None
	intr= [ExtendedInterpolation, BasicInterpolation, no]
	opts = {
		'delimiters': (':', '='),
		'allow_no_value': True,
		'strict': False
		}
	i=0
	r=read(i)
	if r == False:
		a=RawConfigParser(**opts)
		a.optionxform = lambda option: option
		try:
			r = Clict()
			a.read(file)
			cfg=a
			for sec in cfg:
				for key in cfg[sec]:
					r[sec][key]=cfg[sec][key]
		except Exception as E:
			r=False
		

		
	return r
	



# def readConfig(file):
# 	def testconfig(c):
# 		result=False
# 		with suppress(Exception):
# 			for section in c:
# 				for key in c[section]:
# 						test=c[section][key]
# 				return True
# 		return result
#
# 	opts={'delimiters':(':', '='), 'allow_no_value':True}
# 	CEI = lambda : ConfigParser(interpolation=ExtendedInterpolation(),**opts,strict=False)
# 	CBI = lambda : ConfigParser(interpolation=BasicInterpolation(),**opts)
# 	CNI = lambda : ConfigParser(interpolation=None,**opts)
# 	CRP = lambda : RawConfigParser(**opts,strict=False)
#
# 	cfg=None
# 	i=0
# 	while i<4:
# 		cfg = [CEI,CBI,CNI,CRP][i]()
# 		parser=['extended','basic','none','raw'][i]
# 		cfg.optionxform = lambda option: option
# 		cfg.read(file)
# 		if testconfig(cfg):
# 			result=[CEI,CBI,CNI,CRP][i]()
# 			result.optionxform = lambda option: option
# 			result.read(file)inc
# 			break
# 		else:
# 			i+=1
#
# 	return cfg

class Config(Clict):
	__module__ = Clict
	__qualname__ = "ClictConfig"
	__version__ ='0.1.01'
	def __init__(__s,*a,**k):
		__s._self=self
		__s.__args__(*a)
		__s.__kwargs__(**k)
		super().__init__()
		__s.__readconfig__()

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

		__s=CheckFile(__s)

	def __opts__(__s,**opts):
		__s._opts.strip_fileSuffix = True
		__s._opts.strip_filePrefix = True
		__s._opts.strip_folderPrefix = True
		__s._opts.strip_folderSuffix = True
		__s._opts.split_onUnderscore = True
		__s._opts.exclude.file.prefix = ['.','_']
		__s._opts.exclude.file.suffix= ['.bak','.old','.disabled']
		__s._opts.exclude.folder.prefix = ['.','_']
		__s._opts.include.file.suffix= ['.conf','.config','.init', '.ini', '.cfg','.toml','.profile']

	def __readconfig__(__s):
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
					__s[name] = Config(self=s, opts=__s._opts)
				elif len(item.suffix) != 0:
					__s[item.suffix[1:]][name]=Config(self=s, opts=__s._opts)
				else:
					__s[name] = Config(self=s, opts=__s._opts)


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
