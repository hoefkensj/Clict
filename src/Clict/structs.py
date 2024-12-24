#!/usr/bin/env python
import os

from Clict.Typedef import ClictBase
from dataclasses import dataclass,field
from pathlib import Path
from subprocess import getoutput





class Stat:
	def __init__(__s,path,**sel):
		p=Path(path).expanduser().resolve()
		__s.exists = p.exists()
		__s.file = p.is_file()
		__s.folder = p.is_dir()
		__s.ftype=getoutput(f'file {p}').split(':')[-1].split()


@dataclass()
class Self():
	path:Path=field(default=None)
	name:str=field(default='')
	parent:callable=field(default=None)
	cat:list[str]=field(default=None)
	type:Stat=field(default=None)
	def __post_init__(__s):
		if __s.path is not None:
			if not isinstance(Path,__s.path):
				__s.path=Path(__s.path)
				__s.
			__s.name=__s.path.name
			__s.parent=Path(__s.path.parent)
			__s.cat=



		
		
		
stat=ClictBase()
stat.is_real=None
stat.is_virt=None
stat.is_file=None
stat.is_folder=None
stat.is_config=None


opts=ClictBase()
opts.str_color=None
opts.str_multi=None
opts.rep_tree=None
opts.rep_color=None

