from pathlib import Path
from subprocess import getoutput
from enum import property,IntFlag
class Stat:
	def __init__(__s,path,**sel):
		p=Path(path).expanduser().resolve()
		__s.exists = p.exists()
		__s.file = p.is_file()
		__s.folder = p.is_dir()
		__s.symlink=p.is_symlink()
		__s.ftype=getoutput(f'file {p}').split(':')[-1].split()

class Flags(IntFlag):
		strip_file_Suffix   = 1
		strip_file_Prefix   = 2
		strip_folder_Prefix = 4
		strip_folder_Suffix = 8
		split_on_Underscore = 16
		split_on_dot        = 32
		split_on_dash       = 64
