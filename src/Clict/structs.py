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



class Self():
	def __init__(__s,**self):
		p=Path(self.get('path','root://'))
		__s.name=self.get('name',p.name)
		__s.suffix = p.suffix
		__s.stem = p.stem
		__s.parent=lambda:self.get('parent')
		__s.path=Path(p,__s.name)
		__s.cat=[]
		__s.type=Stat(__s.path)




		
		
		
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

