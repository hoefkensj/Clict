
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
from Clict.base.clict import Clict as clictbase
from contextlib import suppress
from Clict.clictConfig.types import Stat, OptFlag, ConfSelf, ConfOpts
import inspect
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

class Config(Clict):
	__module__ = Clict
	__qualname__ = "ClictConfig"
	__version__ ='0.2.01'
	_self:ConfSelf

	def __init__(__s,*a,**k):
		path=k.get('path')
		if not k.pop('ischild',False):
			k['isroot']=True
			if (len(a)==1) * (not k.get('path',False)):
				if (isinstance(a[0],str)+(isinstance(a[0],Path))) :
					path=a[0]
			k['path']=path

		__s.__args__(*a)
		__s.__kwargs__(**k)

		__s.__load__()
		
	def __self__(__s,*a,**s):
		self= s.pop('self',None)
		path= s.get('path')
		isroot= s.get('isroot')
		if isinstance(self,ConfSelf):
			__s._self=self
		else:
			s['path']=path
			if isroot:
				s['root']=path
			__s._self=ConfSelf(**s)

	def __kwargs__(__s,**k):

			__s.__self__(self=k.pop('self',{}),path=k.pop('path',Path()),isroot=k.pop('isroot',False))
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
		# if __s._self.stat.value:
		# 	__s.__isvalue__()

	def __isconfig__(s, path=None):
		def excluded(path):
			byprefix=any([path.name.startswith(prefix) for prefix in s._self.opts.exclude.file.prefix])
			bysuffix=path.suffix not in s._self.opts.exclude.file.suffix
			return bysuffix or byprefix

		result=False
		if path is None:path=s._self.path
		if not excluded(path):
			result=testConfig(path)
		return result

	def __isfolder__(__s):
		def hasconfig(folder):
			result=False

			if not  __s._self.types:
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
				[folder.name.startswith(prefix) for prefix in __s._self.opts.exclude.folder.prefix])
			return result

		files=[Path(it) for it in __s.getself().path.glob('*') if it.is_file()]
		opts = __s.getself().opts.parser.opts
		cfgs=[]
		for file in files:
			if __s.__isconfig__(file):
				cfgs+=[file]
				self=ConfSelf(path=file.resolve(),type='config',types=['file'],stat=Stat(file),parent=__s)
				__s[self.name]=Config(self=self,ischild=True)

			# eval("S['" + "']['".join(partlist) + "']")
		folders=[Path(it) for it in __s.self.path.glob('*') if it.is_dir()]
		for folder in folders:
			if not excluded(folder):
				if hasconfig(folder):
					self=ConfSelf(parent=__s,path=folder,stat=Stat(folder),type='config')
					__s[self.name]=Config(self=self,ischild=True)

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
					cfgself = ConfSelf(name=section, path=(Path(f'{__s._self.path}##{section}')), parser=parser)
					__s[cfgself.name]=Config(self=cfgself,ischild=true)

	def __issection__(__s):
		parser=__s._self.parser
		section=parser[__s._self.name]
		for key in section:
			value=section[key]
			keypath = Path(f'{__s._self.path}$${key}')
			valpath = Path(f'{__s._self.path}::{value}')
			valself = ConfSelf(name='value', value=value, path=valpath, parser=parser, section=section, key=key)
			value = section[key]

			__s[key]=value#.replace('{','[CLICT_REPL_U007B]').replace('}','[CLICT_REPL_U007D]')

	# def __iskey__(__s):
	# 	parser=__s._self.parser
	# 	section=__s._self.section
	# 	key=__s._self.name
	# 	value=parser[section][key]
	# 	path = Path(f'{__s._self.path}::{type(value)}')
	# 	valself=ValueSelf(name='value',value=value,path=path,parser=parser,section=section,key=key)
	# 	__s.value=str(value)#.replace('{','{CLICT_REPL_U007B}').replace('}','{CLICT_REPL_U007D}')

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



class ConfigKey(Config):
	pass

class ConfigVal(str):
	__module__ = Clict
	__qualname__ = "ClictValue"
	__version__ = '0.0.01'

	def __init__(__s, *a, **k):
		__s._self = None
		if a:
			__s._value=''.join(a)
		__s.__self__(**k,)
		super().__init__()
	def __self__(__s, **s):
		self = s.get('self')
		if isinstance(self, ConfSelf):
			__s._self = self
		else:
			s['path'] = s.get('path',)
			s['value']= __s._value
			s['parser'] = s.get('parser')
			s['section'] =  s.get('section')
			s['key'] = s.get('key')
			__s._self = ConfSelf(name='value', **s)


