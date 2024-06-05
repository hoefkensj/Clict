#!/usr/bin/env python
import configparser
from random import randint



class Clict(dict):
	__module__ = None
	__qualname__ = "Clict"
	def __new__(c, *a, **k):
		return super().__new__(c, *a, **k)

	def __init__(s, *a, **k):
		super().__init__( **k)
		if a:
			a=a[0]
			if not isinstance(a,dict):
				raise TypeError
			else:
				s.__convert__(a)

	def __setattr__(s, k, v):
		# print('setattr_called with:' ,f'{k=}{v=}')
		k=s.__expandkey__(k)
		s[k]=v
		# super().__setitem__(k,v)

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
		return super().__getitem__(k)


	def __dict__(s):
		sdict=Clict()
		for attr in super().keys():
			sdict[attr]=s[attr]
		return sdict

	def __missing__(s,k):
		# print('missing called with:' ,f'{k=}')
		missing=Clict()
		missing.__setparent__(s)
		s.__setitem__(k,missing)
		return super().__getitem__(k)

	def __contains__(s, item):

		return (item in s.__dict__().keys())

	def __iter__(s):
		return (i for i in s.__clean__())

	def __hidden__(s):
		result=[]
		hidden=Clict()
		pfx=s.__pfx__()
		for key in [*super().__iter__()]:
			if str(key).startswith(pfx):
				nkey=str(key).removeprefix(pfx)
				nkey=str(nkey).removeprefix('_')
				result+=[nkey]
				hidden[nkey]=s.__getitem__(key)
		return hidden

	def __convert__(s, a):
		for key in a:
			if isinstance(a[key],dict):
				s[key]=Clict(a[key])
			else:
				s[key]=a[key]

	def __setparent__(s,p):
		parent=p
		def ReturnParent(p):
			def returnparent():
				return p
			return returnparent
		s._parent=ReturnParent(p)
		return s._parent

	def __getparent__(s):
		k=s.__expandkey__('_parent')
		return super().get(k)

	def __clean__(s):
		result=[]
		for key in [*super().__iter__()]:
			if not str(key).startswith(s.__pfx__()):
				result+=[key]
		return result

	def __pfx__(s):
		prefix=type(s).__name__
		pfx = f'_{prefix}_'
		return pfx

	def __expandkey__(s, k):
		pfx = s.__pfx__()
		if str(k).startswith('__'):
			k=k
		elif str(k).startswith('_'):
			if not str(k).startswith(pfx):
				k=f'{pfx}{k}'
		return k

	def get(s,k,default=None):
		# print(f'get called with {k}')
		k=s.__expandkey__(k)
		return super().get(k)

	def keys(s):
		return s.__clean__()

	def items(s):
		Items={}
		keys= s.__clean__()
		for key in keys:
			Items[key]=super().__getitem__(key)
		return Items

	def values(s):
		Values=[]
		keys = s.__clean__()
		for key in keys:
			Values += [super().__getitem__(key)]
		return Values

	def __setstrstyle__(s, style):
		styles={
			# 'blackwhite': s.__blackwhitestr__,
			'color': s.__colorstr__,
			'fancy': s.__fancystr__
		}
		mystyle=styles.get(style,styles.get('color'))
		s._strstyle=mystyle
		return  mystyle


	def __str__(s,O='\u007b', C='\u007d'):
		if '_strstyle' in s:
			print('found')
		else:
			return s.__colorstr__()

	def __colorstr__(s,O='\u007b', C='\u007d'):
		def gencolor():
			state = [0, 0, 0]
			rnd= lambda : randint(0, 255)
			rgb= lambda : randint(0, 2)
			state=[rnd(),rnd(),rnd()]
			while sum(state) < 383:
				 state[rgb()]=rnd()
			return [str(i) for i in state]
		COLOR=gencolor()
		ANSI = '\x1b[0;38;2;{COLOR}m{TXT}\x1b[m'.format(COLOR=';'.join(COLOR),TXT='{TXT}')
		BRACES='\x1b[1;38;2;{COLOR}m{TXT}\x1b[m'.format(COLOR=';'.join(COLOR),TXT='{TXT}')
		O=BRACES.format(TXT=O)
		C=BRACES.format(TXT=C)
		ITEMS=[]
		for item in s.keys():
			KEY=ANSI.format(TXT=item)
			VAL=super().__getitem__(item)
			if isinstance(VAL,str):
				VAL=ANSI.format(TXT=repr(VAL))
			ITEMS += ['{KEY} : {VAL}'.format(KEY=KEY, VAL=VAL)]
		ITEMS=','.join(ITEMS)
		retstr='{O}{TXT}{C}'.format(TXT=ITEMS,O=O,C=C)
		return retstr

	def __fancystr__(s):
		from textwrap import shorten

		def pTree(*a, **k):
			def keydash():
				dash='┣'*(keys!=0)+'┗'*(keys==0)
				return dash
		def fcol(string,icol):
			return f'\x1b[{icol}m{string}\x1b[m'
			fstr = ''
			d = a[0]
			maxd = a[1] if len(a) > 1 else 0
			limi = k.get("limit") or (a[2] if len(a) > 2 else 0)
			depth = k.get("depth") or 0
			keys = len(d.keys())
			depthstop = True if (maxd == depth and not maxd <= 0) else False
			limstop = True if (len(d) >= limi and not limi <= 0) else False
			if limstop or depthstop:
				overview(d)
			else:
				for key in d:
					dkey = fcol(shorten(d[key] if callable(d[key]) else str(d[key]), 80),32)
					keys -= 1
					if isinstance(d[key], dict):
						fstr += f'\n{"┃" * depth}'
						fstr += f'{keydash()}━━{fcol(str(key),34)}:'
						fstr += pTree(d[key], maxd, limi, depth=depth + 1)

					else:
						fstr += "\n"
						fstr += "┃" * (depth)
						fstr+= f'{keydash()}━━\t:\t\x1b[1;33m{dkey}\x1b[m'
			return fstr
		return pTree(s)