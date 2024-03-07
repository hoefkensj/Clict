#!/usr/bin/env python
class Clict(dict):
	def __new__(c, *a, **k):
		return super().__new__(c, *a, **k)
	def __init__(s, *a, **k):
		super().__init__(*a, **k)
	def __setattr__(s, k, v):
		if k.startswith('__'):
			k=f'_{s.__class__.__name__}{k}'
		s[k]=v
	def __getattr__(s, k):
		if k.startswith('__'):
			k=f'_{s.__class__.__name__}{k}'
		try:
			return s[k]
		except KeyError as e:
			raise AttributeError(e)
	def __dict__(s):
		return super.__dict__()
	def __missing__(s,k):
		super().__setitem__(k,Clict())
		s[k].__parent__=s
		return super().__getitem__(k)
	def __contains__(s, item):
		return super().__getitem__(item)

	def __get__(s, k, default=None):
		try:
			return super().__getitem__(k)
		except KeyError:
			return default
	def __iter__(s):
		siter=[*super().__iter__()]
		hide='_'+s.__class__.__name__+'_'
		hidden= (item for item in siter if not str(hide) in str(item))
		return hidden

	def keys(s):
		skeys = [*super().keys()]
		hide = '_' + s.__class__.__name__ + '_'
		hidden = [item for item in skeys if not str(hide) in str(item)]
		return hidden

	def __str__(s):
		KV=' {KEY}:{VAL}'
		RT='{O}{TXT}{C}'
		QU="'{TXT}'"
		ret=[]
		OC={'O':'{O}','C':'{C}'}
		for item in s:
			VAL=s[item]
			if isinstance(s[item],str):
				VAL=QU.format(TXT=s[item])
			KEY=item
			ret+=[KV.format(KEY=KEY,VAL=VAL,**OC)]
		ret=RT.format(TXT=','.join(ret),O='\u007b',C='\u007d')
		return ret

