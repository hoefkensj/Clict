#!/usr/bin/env python
class Clict(dict):
	def __clean__(s):
		cname=s.__class__.__name__
		pfx=f'_{cname}_'
		result=[]
		for key in super().__iter__():

			if not str(key).startswith(pfx):
				result+=[key]
		return result

	def __expandkey__(s,k):
		if k.startswith('__'):
			cname = s.__class__.__name__
			pfx = f'_{cname}_'
			k=k.replace('_',pfx,1)
		return k
	def __new__(c, *a, **k):
		return super().__new__(c, *a, **k)
	def __init__(s, *a, **k):
		super().__init__(*a, **k)
	def __setattr__(s, k, v):
		ek=s.__expandkey__(k)
		s[ek]=v
	def __getattr__(s, k):
		ek=s.__expandkey__(k)
		try:
			return s[ek]
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
		return (i for i in s.__clean__())


	def keys(s):
		skeys = [*super().keys()]
		hide = '_' + s.__class__.__name__ + '_'
		hidden = [item for item in skeys if not str(hide) in str(item)]
		return hidden

	def __str__(s,O='\u007b', C='\u007d'):
		ret=[]
		for item in s.keys():
			VAL=s[item]
			if isinstance(s[item],str):
				VAL = "'{TXT}'".format(TXT=s[item])
			ret += ['{KEY}:{VAL}'.format(KEY=item, VAL=VAL)]
		ret = '{O}{TXT}{C}'.format(TXT=','.join(ret),O=O,C=C)
		return ret

	def __parents__(s, *keys):
		current = s
		for key in keys:
			for part in key.split('.'):
				current = current[part]
	def fromsplit(s,name,symbol):
		if symbol in name:
			names=name.split(symbol)
			while names:
				parent=names.pop(0)
				s[parent]=Clict().fromsplit(symbol.join(names),symbol)
		else:
			s[name]=Clict()
		return s