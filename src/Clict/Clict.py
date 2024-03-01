#!/usr/bin/env python
class Clict(dict):
	def __new__(c, *a, **k):
		return super().__new__(c, *a, **k)
	def __init__(s, *a, **k):
		super().__init__(*a, **k)
	def __setattr__(s, k, v):
		s[k]=v
	def __missing__(s,k):
		n=Clict()
		n.__setname__(k)
		n.__setparent__(s)
		super().__setitem__(k,n)
		return super().__getitem__(k)
	def __getattr__(s, k):
		return super().__getitem__(k)
	def __dict__(s):
		dct=super().__dict__()
		for k in {**dct}:
			if k.startswith('__'):
				dct.pop(k)
		return dct
	def __contains__(s, item):
		return super().__getitem__(item)
	def __setname__(s, name):
		s['__name']=name
	def __setparent__(s, parent):
		s['__parent']=parent
	def __parents__(s,*k):
		keys=[]
		for key in k:
			keys+=key.split('.')
		this=keys.pop(0)
		s[this] = Clict()
		if len(keys)>0:
			s[this].__parents__(*keys)
	def get(s, k):
		if k in s:
			return super().__getitem__(k)
		else:
			return None
