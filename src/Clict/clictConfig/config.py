
#!/usr/bin/env python
import os
import sys
from logging import exception
from re import escape,findall
if not os.name=='nt':
	import termios
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser
from Clict.Clict import Clict
from Clict.base.Clict import Clict as clictbase
from contextlib import suppress
from Clict.clictConfig.types import Stat, OptFlag, ConfSelf, ConfOpts,ValueSelf


# def check_Config(file,opts):
# 	def read(i):
# 		intr = [ExtendedInterpolation, BasicInterpolation, no]
# 		cfg = ConfigParser(interpolation=intr[i](),**opts)
# 		cfg.optionxform = lambda option: option
# 		try:
# 			result = Clict()
# 			cfg.read(file)
# 			for sec in cfg:
# 				for key in cfg[sec].keys():
# 					result[sec][key]=cfg[sec][key]
# 		except Exception as E:
# 			return False
# 		return intr[i]
#
# 	no=lambda :None
# 	cfg=False
# 	i=0
# 	r=read(i)
# 	while cfg == False:
# 		if i < 2:
# 			i+=1
# 			interpol = read(i)
# 		else:
# 				a=RawConfigParser(**opts)
# 				a.optionxform = lambda option: option
# 				a.read(file)
# 				cfg=a
# 				break
#
# 	return cfg
def testConfig(path):
	def Parser():
		parser = RawConfigParser(**{
			'delimiters': (':', '='),
			'allow_no_value': True,
			'strict': False
		})
		parser.optionxform = lambda option: option
		return parser
	def test(file):
		try:
			parser=Parser()
			parser.read(file)
			valid=True
			fallback=parser
		except Exception:
			valid=False
			fallback=None
		return valid

	return test(path)
#
#

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
	__version__ ='0.2.01'

	def __init__(__s,*a,**k):
		__s._self=None
		__s.__args__(*a)
		__s.__kwargs__(**k)
		
		__s.__load__()
		
	def __self__(__s,**s):
		self= s.get('self')
		path= s.get('path')
		if isinstance(self,ConfSelf):
			__s._self=self
		else:
			s['path']=path
			__s._self=ConfSelf(**s)

	def __kwargs__(__s,**k):
			__s.__self__(self=k.pop('self',{}),path=k.pop('path',Path()))
			super().__kwargs__(**k)

	def __load__(__s):
		if __s._self.stat.folder:
			__s.__isfolder__()
		if __s._self.stat.file:
			__s.__isfile__()
		if __s._self.stat.section:
			__s.__issection__()
		if __s._self.stat.key:
			__s.__iskey__()
		if __s._self.stat.value:
			__s.__isvalue__()

	def __isconfig__(s, path=None):
		def excluded(path):
			byprefix=any([path.name.startswith(prefix) for prefix in s._self.opts.exclude.file.prefix])
			bysuffix=path.suffix not in s._self.opts.exclude.file.suffix
			return bysuffix or byprefix

		result=False
		if path is None:path=s._self.path
		result=testConfig(path)*excluded(path)
		return result

	def __isfolder__(__s):
		def hasconfig(folder):
			result=False
			if not __s._self.type=='config':
				files=folder.rglob('*')
				for f in files:
					if f.suffix in __s._self.opts.include.file.suffix:
						result=True
						break
			else:
				result=True
			return result

		def excluded(folder):
			result= folder.suffix  in __s._self.opts.exclude.file.suffix or any(
				[folder.name.startswith(prefix) for prefix in __s._self.opts.exclude.file.prefix])
			return result

		files=[Path(it) for it in __s.self().path.glob('*') if it.is_file()]
		opts = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}
		cfgs=[]
		for file in files:
			if __s.__isconfig__(file):
				cfgs+=[file]
				self=ConfSelf(path=file.resolve(),type='config',types=['file'],stat=Stat(file),parent=__s)
				__s[self.name]=Config(self=self)

			# eval("S['" + "']['".join(partlist) + "']")
		folders=[Path(it) for it in __s.self().path.glob('*') if it.is_dir()]
		for folder in folders:
			if not excluded(folder):
				if hasconfig(folder):
					self=ConfSelf(parent=__s,path=folder,stat=Stat(folder),type='config')
					__s[self.name]=Config(self=self)

	def __isfile__(__s):
		opts = __s._self.opts
		file=__s._self.path
		parsers=['ext','bas','non','raw']
		success=False
		i=0
		while True:
			parser=__s.__getparser__(parsers[i])
			try:
				parser.read(file)
				for section in parser:
					for key in parser[section]:
						str(parser[section][key])
				success=True
			except Exception:
				success=False

			if success is False and i < 3:
				i+=1
				continue
			else:
				break
		if success is True:
			for section in parser:
				if not  section=='DEFAULT':
					path=Path(f'{__s._self.path}##{section}')
					cfgself=ConfSelf(name=section,path=path,parser=parser)
					__s[cfgself.name]=Config(self=cfgself)

	def __issection__(__s):
		parser=__s._self.parser
		section=parser[__s._self.name]
		for key in section:
			path = Path(f'{__s._self.path}$${key}')
			value = section[key]
			path = Path(f'{__s._self.path}::{type(value)}')
			valself = ValueSelf(name='value', value=value, path=path, parser=parser, section=section, key=key)

			__s[key]=value#.replace('{','[CLICT_REPL_U007B]').replace('}','[CLICT_REPL_U007D]')

	def __iskey__(__s):
		parser=__s._self.parser
		section=__s._self.section
		key=__s._self.name
		value=parser[section][key]
		path = Path(f'{__s._self.path}::{type(value)}')
		valself=ValueSelf(name='value',value=value,path=path,parser=parser,section=section,key=key)
		__s.value=str(value).replace('{','{CLICT_REPL_U007B}').replace('}','{CLICT_REPL_U007D}')

	def __getparser__(s,parser):
		opts = s._self.opts.parser.opts
		rawparser=RawConfigParser(**opts)
		rawparser.optionxform = lambda option: option
		extparser=ConfigParser(interpolation=ExtendedInterpolation(), **opts)
		extparser.optionxform = lambda option: option
		basparser=ConfigParser(interpolation=BasicInterpolation(), **opts)
		basparser.optionxform = lambda option: option
		nonparser=ConfigParser(interpolation=None, **opts)
		nonparser.optionxform = lambda option: option
		parsers={'ext':extparser,'bas':basparser,'non':nonparser,'raw':rawparser}
		return parsers[parser]



