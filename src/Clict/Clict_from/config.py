
#!/usr/bin/env python
import os
import sys
import termios
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser
from Clict.Clict import Clict
from contextlib import suppress
from Clict.structs import Self   ,Stat




def check_Config(file,opts):
	def read(i):
		intr = [ExtendedInterpolation, BasicInterpolation, no]
		cfg = ConfigParser(interpolation=intr[i](),**opts)
		cfg.optionxform = lambda option: option
		try:
			result = Clict()
			cfg.read(file)
			for sec in cfg:
				for key in cfg[sec].keys():
					result[sec][key]=cfg[sec][key]
		except Exception as E:
			return False
		return intr[i]
		
	no=lambda :None
	cfg=False
	i=0
	r=read(i)
	while cfg == False:
		if i < 2:
			i+=1
			interpol = read(i)
		else:
				a=RawConfigParser(**opts)
				a.optionxform = lambda option: option
				a.read(file)
				cfg = Clict()
				cfg=a
				break

	return cfg
	



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

class Config():
	__module__ = Clict
	__qualname__ = "ClictConfig"
	__version__ ='0.1.01'
	def __init__(__s,path=None,*a,**k):
		__s._self=Self(path)
		__s.__args__(*a)
		__s.__kwargs__(**k)
		
		__s._self=Self(__s._tmp.path)
		super().__init__()
		

		# __s.__type__()

	def __kwargs__(__s,**k):
		


		__s.__inspect__()
		__s.__type__()
	def __args__(__s,*a):
		for path in a[::-1]:
			__s._tmp.path=Path(path)


	def __inspect__(__s):
			isexclude = lambda t: t.casefold() in __s._opts.exclude.file.prefix
			isdisabled = lambda n: n.startswith('_')
			p=__s._self.path
			__s._self.type.config=__s.__iscfg__()
			__s._self.type.ignore= isexclude(t=p.suffix)
			__s._self.type.disable= isdisabled(p.name)
			
	def __iscfg__(__s,file=None):
		path=__s._self.path
		if file is not None:
			path=Path(file)
		
		try:
			tmp = RawConfigParser(**{
				'delimiters': (':', '='),
				'allow_no_value': True,
				'strict': False
				})
			tmp.read(path)
			
			for section in tmp:
				for key in tmp[section]:
					_=tmp[section][key]
			res=True
		except Exception:
			res=False
		return 	res
	
	def __type__(__s):
		if __s._self.type.folder:
			__s.__folder__()
		elif __s._self.type.file:
			__s.__readconfig__()
			
	def __opts__(__s):
		
		__s._opts.strip_fileSuffix = True
		__s._opts.strip_filePrefix = True
		__s._opts.strip_folderPrefix = True
		__s._opts.strip_folderSuffix = True
		__s._opts.split_onUnderscore = True
		__s._opts.exclude.file.prefix = ['.','_']
		__s._opts.exclude.file.suffix= ['.bak','.old','.disabled']
		__s._opts.exclude.folder.prefix = ['.','_']
		__s._opts.include.file.suffix= ['.conf','.config','.init', '.ini', '.cfg','.toml','.profile']
		__s._opts.parser= {'delimiters': (':', '='), 'allow_no_value': True ,		'strict': False}

	def __readconfig__(__s):


				c=Clict()
				if __s._self.type.get('config'):
					cfg=check_Config(__s._self.path,__s._opts.parser)

					for section in cfg:
						if section == 'DEFAULT':
							continue
						for key in cfg[section]:
							if key in cfg['DEFAULT']:
								if cfg['DEFAULT'][key] == cfg[section][key]:
									continue
							c[section][key] = cfg[section][key]
						__s[section][key] = cfg[section][key]
	
					# 	if len(c[section])==0:
					# 		c[section]=str(None)
					# if len(c)==0:
					# 	c=None
					# else:
					# 	for section in c:
					# 		for key in c[section]:
					# 			=c[section][key]
		# #
		# else:
		# 	__s.error=f'{__s._self.get("path")} : exists = {__s._self.type.exists}'
		# 	# print(, 'is not a config',__s.error)
		#



	def __folder__(__s):
		itemlist = [*__s._self.path.glob('*')]
		for item in [*__s._self.path.glob('*')]:
			if item.is_dir() or  __s.__iscfg__(item):
				s=Self(item)
				__s[item.name]= Config(item, opts=__s._opts)
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
