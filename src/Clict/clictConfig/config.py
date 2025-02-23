
#!/usr/bin/env python
import os
import sys
from re import escape,findall
if not os.name=='nt':
	import termios
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser
from Clict.Clict import Clict
from contextlib import suppress
from Clict.types.self import ConfSelf,ConfOpts
from Clict.clictConfig.types import Stat,OptFlag


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
				cfg=a
				break

	return cfg
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
		__s.__self__(**k.pop('self',{}))
		__s.__args__(*a)
		__s.__kwargs__(**k)
		
		__s.__load__()
		
	def __self__(__s,**self):
		name=self.get('name')
		parent=self.get('parent')
		path=Path(self.get('path'))
		stat=Stat(path)
		type='Config'
		opts=self.get('opts',ConfOpts())
		__s._self=ConfSelf(name=name,parent=parent,path=path,stat=stat,type=type,opts=opts)


	def __load__(__s):
		if __s._self.stat.folder:
			__s.__isfolder__()
		if __s._self.stat.file:
			__s.__isfile__()
		if __s._self.type == 'section':
			__s.__issection__()
		# elif __s._self.stat.file:
	def __isconfig__(s, path=None):
		if path is None:
			path=s._self.path
		if path.suffix not in s._self.opts.exclude.file.suffix and not any([path.name.startswith(prefix) for prefix in s._self.opts.exclude.file.prefix]):
			result=testConfig(path)
		else:
			result=False
		return result

	# 	__s.__isfile__()
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

		# for item in [it for it in  __s.self().path.glob('*') if  it.absolute().name[0] not in ['_','.']]:
		files=[Path(it) for it in __s.self().path.glob('*') if it.is_file()]
		opts = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}
		cfgs=[]
		for file in files:
			if __s.__isconfig__(file):
				cfgs+=[file]
				self=ConfSelf(path=file.resolve(),stat=Stat(file),parent=__s)
				__s[self.name]=Config(self=self)

			# eval("S['" + "']['".join(partlist) + "']")
		folders=[Path(it) for it in __s.self().path.glob('*') if it.is_dir()]
		for folder in folders:
			if not excluded(folder):
				if hasconfig(folder):
					self=ConfSelf(parent=__s,path=folder,stat=Stat(folder))
					__s[self.name]=Config(self=self)


			# 	partlist+=[{part:Config(self={'name':part,'path':Path(part)})}]
			# for part in partlist:
			# 	s[[*part.keys()][0]]=[*part.values()][0]
			# 	s=s[[*part.keys()][0]]
			# 	print(s)
			#
			#






			#
			# 		cfg=Config(self=self)
			# 		__s[cfg.self().name]=cfg
			# elif item.is_file() and __s.__isconfig__(item):
			# 	# best=GetBestParser(item)
			# 	# self.parse=best
			# 	# opts = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}
			# 	# parse = ConfigParser(interpolation=best(), **opts)
			# 	# parse.optionxorm = lambda option: option
			# 	cntent={}
			# 	def parse(path):
			# 		with open(path,'r') as f:
			# 			cntent= {i:line for i,line in enumerate(f)}
			# 	# cl=Clict(parse.read(item))
			# 	cl=Clict(**cntent)
			# 	cfg=Config(cl,self=self)
			# 	__s[cfg.self().name] = cfg




	def __isfile__(__s):
		opts = __s._self.opts.delimiters
		file=__s._self.path
		Interpolation=GetBestInterpolation(file)
		if not isinstance(Interpolation, RawConfigParser):
			parser = ConfigParser(interpolation=Interpolation(), **opts)
			parser.optionxorm = lambda option: option
		else:
			parser=Interpolation
		parser.read(file)
		for section in parser:
			if section=='DEFAULT':
				continue
			else:
				path=Path(__s._self.path,'#',section)
				dct={}
				for key in parser[section]:
					dct[key]=parser[section][key]
				__s[section]=Config(self=ConfSelf(name=f'{__s.path.name}#{key}',path=path,stat=Stat(path),type='section',types='section'),**dct)

	def __issection__(__s):
		print('works')

def GetBestInterpolation(path):
	def rawParser():
		parser = RawConfigParser(**{
			'delimiters': (':', '='),
			'allow_no_value': True,
			'strict': False
		})
		parser.optionxform = lambda option: option
		return parser
	def testreadconfig(opts={	'delimiters': (':', '='),'allow_no_value': True,'strict': False}):

		def Parser(i):
			interpol=[ExtendedInterpolation, BasicInterpolation, no:=lambda :None]
			parser = ConfigParser(interpolation=interpol[i](), **opts)
			parser.optionxform = lambda option: option
			return parser
		parsers=[]
		for i in range(2):
			parser=Parser(i)
			try:
				parser.read(path)
				for section in parser:
					if section=='DEFAULT':
						continue
					else:
						for key in parser[section]:
							parser[section][key]

				parsers+=[[ExtendedInterpolation, BasicInterpolation, no:=lambda :None][i]]
			except Exception:
				pass


		return parsers
	bestparser=rawParser()
	parsers=testreadconfig()
	if len(parsers)>0:
		bestparser=parsers[0]
	return bestparser


class ConfigSection(Clict):
	__module__ = Clict
	__qualname__ = "ClictConfigSection"
	__version__ = '0.2.01'

	def __init__(__s, path=None, *a, **k):
		__s._self = None
		__s.__self__(**k.pop('self', {}))
		__s.__args__(*a)
		__s.__kwargs__(**k)

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



	# def __folder__(__s):
	# 	itemlist = [*__s._self.path.glob('*')]
	# 	for item in [*__s._self.path.glob('*')]:
	# 		self=Self(item)
	# 		if (self.stat.folder)*(not self.stat.symlink) :
	# 			s=Self(item)
	# 			__s[item.name]= Config(item, self=s)
a=Config(self={'path':'../../..'})
print(repr(a))