#!/usr/bin/env python
import configparser
from random import randint
class Clict(dict):
	def __new__(c, *a, **k):

		return super().__new__(c, *a, **k)

	def __init__(s, *a, **k):
		# if a:
			# s.__convert__(*a)
		super().__init__(*a, **k)

	def __setattr__(s, k, v):
		# print('setattr_called with:' ,f'{k=}{v=}')
		k=s.__expandkey__(k)
		s[k]=v
		super().__setitem__(k,v)

	def __getattr__(s, k):
		# print('getattr_called with:', f'{k=}')
		k = s.__expandkey__(k)
		return super().__getitem__(k)

	def __setitem__(s, k, v):
		# print('setitem_called with:' ,f'{k=}{v=}')
		k=s.__expandkey__(k)
		super().__setitem__(k,v)

	def __getitem__(s,k,default=None):
		# print('getitem_called with:' ,f'{k=}')
		k=s.__expandkey__(k)
		return super().__getitem__(k)

	def __get__(s, k, default=None):
		# print('__get__ called with:' ,f'{k=}{default}')
		k=s.__expandkey__(k)

	def __dict__(s):
		sdict={}
		for attr in super().keys():
			sdict[attr]=s[attr]
		return sdict

	def __missing__(s,k):
		# print('missing called with:' ,f'{k=}')
		s.__setitem__(k,Clict())
		return super().__getitem__(k)

	def __contains__(s, item):

		return (item in s.__dict__().keys())

	def __iter__(s):
		return (i for i in s.__clean__())

	# def __convert__(s,*a):
	# 	def unpack(currentitem):
	# 		if isinstance(currentitem,dict):
	# 			for key in item:
	# 				if isinstance(item[key],dict):
	# 					clict[key]=s.__convert__(item[key])
	# 				else:
	# 					clict[key]=item[key]
	# 		elif isinstance(currentitem,list):
	# 			for item in currentitem:
	# 				if type(item).__name__ in ['dict','list','set','tuple']:
	# 	clict=Clict()
	# 	for item in a:
	# 		s|=unpack(item)


	def __setparent__(s,*func):
		s.__parent=func

	def __getparent__(s):
		return s.__parent()

	def __clean__(s):

		result=[]
		for key in super().__iter__():
			if not str(key).startswith(s.__pfx__()):
				result+=[key]
		return result

	def __pfx__(s):
		classname=s.__class__.__name__
		pfx = f'_{classname}_'
		return pfx

	def __expandkey__(s,k):

		if str(k).startswith('__'):
			k=k.replace('_', s.__pfx__(), 1)
		return k

	def get(s,k,default=None):
		k=s.__expandkey__(k)
		return super().get(k)

	def keys(s):
		return s.__clean__()

	def __str__(s,O='\u007b', C='\u007d'):
		RND='0;0;0'
		COLS=[[119,52,234], [0,167,234], [138,232,0],[250,241,0], [255,170,0],[255,0,97]]
		while RND=='0;0;0':
			RND=';'.join([str(COLS[randint(2,4)][0]),str(COLS[randint(0,5)][1]),str(COLS[randint(0,5)][2])])
		ANSI = '\x1b[{W};38;2;{RND}m{TXT}\x1b[m'.format(W=randint(0,1),RND=RND,TXT='{TXT}')
		COL=ANSI.format(TXT=':')
		O=ANSI.format(TXT=O)
		C=ANSI.format(TXT=C)
		ITEMS=[]
		for item in s.keys():
			VAL=super().__getitem__(item)
			if isinstance(VAL,str):
				VAL=repr(VAL)
			KEY=ANSI.format(TXT=item)
			ITEMS += ['{KEY} {COL} {VAL}'.format(KEY=KEY, COL=COL, VAL=VAL)]
		ITEMS=','.join(ITEMS)
		retstr='{O}{TXT}{C}'.format(TXT=ITEMS,O=O,C=C)
		return retstr

	# def __parents__(s, *keys):
	# 	current = s
	# 	for key in keys:
	# 		for part in key.split('.'):
	# 			current = current[part]
	# def fromsplit(s,name,symbol):
	# 	if symbol in name:
	# 		names=name.split(symbol)
	# 		while names:
	# 			parent=names.pop(0)
	# 			s[parent]=Clict().fromsplit(symbol.join(names),symbol)
	# 	else:
	# 		s[name]=Clict()
	# 	return s