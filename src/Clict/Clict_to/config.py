#!/usr/bin/env python
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation
def newConfig():
	cfg = ConfigParser(interpolation=None,
										 delimiters=(':'),
										 allow_no_value=True)  # create empty config
	cfg.optionxform = lambda option: option
	return cfg

def Config(c,p):
	p=Path(p).expanduser().resolve().absolute()
	if c._self.get('suffix'):
		p=Path(f'{str(p)}.{ c._self.suffix}')
	isdict=[]
	for item in c:
		for sub in c[item]:
			if isinstance(c[item].get(sub),dict) :
				isdict+=[True]
			else:
				isdict+=[False]
	if all(isdict):
		for item in c:
			to_config(c[item],Path(p,item.replace('_','.')))
	else:
		if not  p.exists():
			Path(p.parent).mkdir(0o777,True,exist_ok=True)
			p.touch(mode=0o666,exist_ok=True)


		cfg=newConfig()
		for section in c:
			cfg.add_section(section)
			for key in c[section]:
				cfg[section][key]=str(c[section][key])
		with open(p,'w') as f:
			cfg.write(f)



