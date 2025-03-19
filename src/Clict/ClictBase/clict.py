#!/usr/bin/env python
from jinja2.nodes import args_as_const

from Clict.ClictBase.base import Clict as ClictBase
from Clict.ClictSelf.base import Self
from Clict.ClictBase.support import TemplateString
from Clict.lib.fnText import CStr
import inspect, re
from Clict.from_other.types import fromList,fromDict



class Clict(ClictBase):
	__module__ = None
	__qualname__ = "Clict"
	__version__ = '0.8.1'
	__clict__='ClictBase.clict.Clict'
	_self : Self=None

	def __init__(__s, *a, **k):
		__s.__self__(*a,**k)
		__s.__args__(__s._self.args)
		__s.__kwargs__()


	def __self__(__s,*a, **k):
		__s._self=Self(
			obj    = __s,
			parent = k.get('parent'),
			name   = k.get('name'),
			args   = a,
			kwargs = k,	)

	def __args__(__s):
		print(__s._self)
		for i, arg in enumerate(a):
			if isinstance(arg, dict):
				dct = fromDict(arg)
				for key in dct:
					__s[key] = dct[key]
			elif isinstance(arg, list):
				dct = fromList(arg)
				for key in dct:
					__s[i][key] = dct[key]
			else:
				__s[i] = arg


	def getself(__s):
		return getattr(__s,'_self')
	def setself(__s,self):
		__s._self=self


	def values(__s):
		return super()._values()

	def keys(__s):
		return super()._keys()
	def items(__s):
		return super()._items()
	def __missing__(__s, k):
		self={'parent':__s,'name':k}
		# print('missing called with:' ,f'{k=}')
		new = Clict(self=self)
		super().__setitem__(k, new)
		return super().__getitem__(k)

	def __str__(s):
		from Clict.lib.fnterm import info
		term = info()
		if term['istty']:
			if s._self.opts.str.color is True:
				ITEMS = []
				cc = CStr()
				for key in s:
					color = CStr()
					ITEMS += [' {KEY} : {VAL} '.format(KEY= color(key), VAL=color(repr(s[key].__str__())))]
				ITEMS = ','.join(ITEMS)
				retstr = '{O}{TXT}{C}'.format(TXT=ITEMS, O=cc('\u007b'), C=cc('\u007d'))
				result=retstr
			else:
				result= super().__str__()
		else:
			result= super().__str__()
		return result
	def __repr__(s):
		clr = s.getself().opts.repr.colors

		# print(dir(clr.tree))
		from Clict.lib.fnterm import info
		if s._self.prop.repr.tree:
			result=s.__tree__()
			if s._self.prop.repr.color:
				term = info()
			formatted=[]
			if term['istty']:
				width=term['get_size']()['C']
				#line shorthning not implemented yet
				for line in result:
					if s._self.opts.repr.color:
						formatted += [TemplateString(line).format(**clr.tree.tpl).ljust(width)[:width]]
					else:
						formatted += [TemplateString(line).format(**clr.tree.bw).ljust(width)[:width]]
			else:
				for line in result:
					if s._self.opts.repr.color:
						formatted += [TemplateString(line).format(**clr.tree.tpl)]
					else:
						formatted += [TemplateString(line).format(**clr.tree.bw)]

			result='\n'.join(formatted)
		else:
			result=TemplateString(s)
		curframe = inspect.currentframe()
		calframe = inspect.getouterframes(curframe, 2)

		if  calframe[1][3] != '__tree__':

			finresult=str('\x1b[1m{CLRTREE}■{CLRRST}{CLRTIT}{TITLE}{CLRRST}\n'.format(TITLE=s._self.name,**clr.tree.rgb))
			finresult+=TemplateString(result).format(**clr.tree.rgb)
			result=finresult
		return result



	def __tree__(s):
		tpl_key=TemplateString("{CLRTREE}{TREE}{CLRRST}{CLRKEY}{KEY}{CLRRST} :")
		tpl_val=TemplateString("{CLRVAL}{VAL}{CLRRST}")
		tpl_lin=TemplateString("{CLRTREE}{PARENT}{CLRRST}   {LINE}")
		clr=s._self.opts.repr.colors
		SYM=s._self.opts.repr.symbols.tree
		TPL=s._self.opts.repr.templates.tree
		keys = len(s._keys())
		plines = []

		for key in s:
			keys -= 1
			TREE = SYM.lastnode if keys == 0 else SYM.clictnode
			plines += [tpl_key.format(TREE=TREE, KEY=TemplateString(key), **clr.tree.tpl)]
			if not isinstance(s[key], dict) or s[key] == {}:
				val=repr(s[key])
				plines[-1] = plines[-1].replace('┳', '━') + tpl_val.format(VAL=val, **clr.tree.tpl)
			else:
				clines = [line for line in repr(s[key]).split('\n') if not line.rstrip()=='']
				for l, line in enumerate(clines):
					clines[l] = tpl_lin.format(PARENT=SYM.parent, LINE=line, **clr.tree.tpl) if keys != 0 else f"    {TemplateString(line)}"
				plines+=clines
		return plines



