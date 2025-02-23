from pathlib import Path
from subprocess import getoutput
from enum import property,IntFlag
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser


def makeParser(**k):
	def makeparser(**k):
		parser =P(**k)
		parser.optionxform = lambda option: option
		def parse(file):
			try:
				parser.read(file)
				result=True
			except Exception :
				result=False
			return result
		return parse
	P=k.get('parser',ConfigParser)
	I=k.get('interpolation', lambda: None)
	D=k.get('delimiters',(':', '='))
	A=k.get('allow_no_value',True)
	S=k.get('strict',False)
	parser=makeparser(interpolation=I(), delimiters=D, allow_no_value=A, strict=S)
	return parser



class Stat:
	def __init__(__s,path,**sel):
		p=Path(path).expanduser().resolve()
		__s.exists = p.exists()
		__s.file = p.is_file()
		__s.folder = p.is_dir()
		__s.symlink=p.is_symlink()
		__s.ftype=getoutput(f'file {p}').split(':')[-1].split()
		__s.config=sel.get('isconfig',None)
		if __s.config==None:
			__s.__isconfig__(p)

	def __isconfig__(__s,p):
			isConfig=makeParser(parser=RawConfigParser)
			__s.config=isConfig(p)

			# __s.config=any([isConfig(i) for i in [it for it in p.rglob('*') if it.is_file()]]







class OptFlag(IntFlag):
		strip_file_Prefix   = 1
		strip_file_Suffix   = 2
		strip_folder_Prefix = 4
		strip_folder_Suffix = 8
		split_on_Underscore = 16
		split_on_dot        = 32
		split_on_dash       = 64
