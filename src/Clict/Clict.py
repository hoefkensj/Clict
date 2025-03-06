#!/usr/bin/env python

from Clict.base.Clict import Clict as ClictBase
from Clict.base.self import Self
from Clict.lib.fnText import CStr
import inspect, re


class Clict(ClictBase):
	__module__ = None
	__qualname__ = "Clict"
	__version__ = '0.7.1'
	
	def __init__(__s, *a, **k):
		__s._self=Self()
		__s.__self__(**k.pop('self',{}))
		__s.__kwargs__(**k)
		super().__init__(*a,**k)

	def __self__(__s,**self):
		__s._self.name=self.get('name')
		__s._self.parent=self.get('parent')

	def self(__s):
		return getattr(__s,'_self')
	def getParent(__s):
		return __s.self().parent
	def values(__s):
		return super()._values()
	
	def keys(__s):
		return super()._keys()
	def items(__s):
		return super()._items()
	def __missing__(__s, k):
		# print('missing called with:' ,f'{k=}')
		missing = Clict(self={'name':k,'parent':__s})
		# missing._self.parent__(__s)
		super().__setitem__(k, missing)
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
					KEY = color(key)
					VAL = s[key]
					if isinstance(VAL, str):
						VAL = color(VAL.__repr__())
					elif isinstance(VAL, dict):
						VAL = VAL.__str__()
					ITEMS += [' {KEY} : {VAL} '.format(KEY=KEY, VAL=VAL)]
				ITEMS = ','.join(ITEMS)
				retstr = '{O}{TXT}{C}{RESET}'.format(TXT=ITEMS, O=cc('\u007b'), C=cc('\u007d'))
				result=retstr
			else:
				result= super().__str__()
		else:
			result= super().__str__()
		return result
	def __repr__(s):
		clr = s._self.opts.repr.colors

		from Clict.lib.fnterm import info
		if s._self.opts.repr.tree:

			result=s.__tree__()
			term = info()
			formatted=[]
			if term['istty']:
				width=term['get_size']()['C']
				#line shorthning not implemented yet
				for line in result:
					if s._self.opts.repr.color:
						formatted += [ValueString(line).format(**clr.tpl)]
					else:
						formatted += [ValueString(line).format(**clr.tree.bw)]
			else:
				for line in result:
					if s._self.opts.repr.color:
						formatted += [ValueString(line).format(**clr.tpl.tpl)]
					else:
						formatted += [ValueString(line).format(**clr.tree.bw)]

			result='\n'.join(formatted)
		else:
			result=ValueString(s)
		curframe = inspect.currentframe()
		calframe = inspect.getouterframes(curframe, 2)

		if  calframe[1][3] != '__tree__':
			result=ValueString(result).format(**clr.tree.rgb)
		return result



	def __tree__(s):
		from Clict.lib.fnterm import info
		clr=s._self.opts.repr.colors
		term = info()
		keys = len(s._keys())
		plines = []
		if term['istty']:
			'''we have a max width now'''

		for key in s:
			keys -= 1
			TREE = "┗━━━┳━╼ " if keys == 0 else "┣━━━┳━╼ "
			plines += [ValueString("{CLRTREE}{TREE}{RESET}{CLRKEY}{KEY}{RESET} :").format(TREE=TREE,KEY=ValueString(key),**clr.tree.tpl)]

			if not isinstance(s[key], dict) or s[key] == {}:
				val=repr(s[key])
				plines[-1] = plines[-1].replace('┳', '━') +ValueString("{CLRVAL}{VAL}{RESET}").format(VAL=val,**clr.tree.tpl)

			else:
				clines = [line for line in repr(s[key]).split('\n') if not line.rstrip()=='']
				for l, line in enumerate(clines):
					clines[l] = ValueString("{CLRTREE}┃{RESET}   {LINE}").format(LINE=line,**clr.tree.tpl) if keys != 0 else f"    {ValueString(line)}"
				plines+=clines
		return plines


class ValueString(str):
	def format(s,**k):
		def substitute(match):
			key = match.group(1)
			if key in k:
				return str(k[key])
			return match.group(0)  # Keep it unchanged if not in mapping

		template=s.__str__()
		prev = None
		while prev != template :  # Stop when no further changes occur
			prev = template
			template = re.sub(r'\{([^{}]+)\}', substitute, template)
		return template

def listtree(lst):
	tree=Clict()
	for i,item in enumerate(lst):
		if isinstance(item,dict):
			tree[i]=treestr(Clict(item))
		else:
			tree[i]=repr(item)
	return tree






