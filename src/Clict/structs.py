#!/usr/bin/env python
import os

from Clict.Typedef import Clict as clictbase
from dataclasses import dataclass,field
from pathlib import Path







		
		
@dataclass
class Clude:
		exclude_file_prefix : list[str]=field(default_factory=lambda :['.','_'])
		exclude_file_suffix= ['.bak','.old','.disabled']
		exclude_folder_prefix = ['.','_']
		include_file_suffix= ['.conf','.config','.init', '.ini', '.cfg','.toml','.profile']




class config_self(Self):
	opts:Opts=field(default=None)
	parser:dict[str|bool] = field(default_factory=lambda :{
		'delimiters': (':', '='),
		'allow_no_value': True,
		'strict': False
		})
	
	def __post_init__(__s):
		if __s.path is not None:
			__s.path=Path()
		if __s.stat.exists:
			__s.path = Path(__s.path).expanduser().resolve()


