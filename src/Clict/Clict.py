#!/usr/bin/env python

from Clict.types.base import Clict as ClictBase
from Clict.types.self import Self
from Clict.lib.fnText import CStr




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
				retstr = '{O}{TXT}{C}\x1b[m'.format(TXT=ITEMS, O=cc('{'), C=cc('}'))
				result=retstr
			else:
				result= super().__str__()
		else:
			result= super().__str__()
		return result
	def __repr__(s):
		from Clict.lib.fnterm import info
		if s._self.opts.repr.tree:
			term = info()
			result=s.__tree__()
			if term['istty']:
				width=term['get_size']()['C']
				for line in result:
					line=line.replace('{','\\u007b').replace('}','\\u007d')
					tpls={i: f'\u007b{i}\u007d' for i in
											  [i.split('}')[0] for i in line.split('{') if
											   '}' in i] if i not in s._self.opts.colors.tree.rgb}
					if len(line.format(**{k:'' for k in s._self.opts.colors.tree.rgb},**tpls))>width :
						line=line[:width-5]+'...'
			else:
				for i,line in enumerate(result):
					line = line.replace('{', '\\u007b').replace('}', '\\u007d')
					tpls = {i: f'\u007b{i}\u007d' for i in
							[i.split('}')[0] for i in line.split('{') if
							 '}' in i] if i not in s._self.opts.colors.tree.rgb}
					result[i]=line.format(**{k:'' for k in s._self.opts.colors.tree.rgb},**tpls)
			result='\n'.join([*result,'\n'])
			result = result.replace('{', '\u007b').replace('}', '\u007d')
			tpls = {i: f'\u007b{i}\u007d' for i in
					[i.split('}')[0] for i in result.split('{') if
					 '}' in i] if i not in s._self.opts.colors.tree.rgb}
			result=result.format(**s._self.opts.colors.tree.rgb,**tpls)
		else:
			result=str(s)
		return result

	def __tree__(s):

		keys = len(s._keys())
		plines = []
		for key in s:
			keys -= 1
			TREE = "┗━━━┳━╼ " if keys == 0 else "┣━━━┳━╼ "
			plines += ["{CLRTREE}{TREE}{CLRRESET}{CLRKEY}{KEY}{CLRRESET} :".format(TREE=TREE,KEY=str(key).replace('{', '\\u007b').replace('}', '\\u007d'),**s._self.opts.colors.tree.tpl)]

			if isinstance(s[key], dict):
				clines = [line.replace('{' ,'[')  for line in repr(s[key]).split('\n') if not line.rstrip()=='']
				for l, line in enumerate(clines):
					clines[l] = "{CLRTREE}┃{CLRRESET}   {LINE}".format(LINE=line.replace('{' ,'['),**s._self.opts.colors.tree.tpl) if keys != 0 else f"    {line}"
				plines+=clines
			else:
				val=repr(s[key])
				plines[-1] = plines[-1].replace('┳', '━') +"{CLRVAL}{VAL}{CLRRESET}".format(VAL=val.replace('{', '\\u007b').replace('}', '\\u007d'),**s._self.opts.colors.tree.tpl)
		return plines





def listtree(lst):
	tree=Clict()
	for i,item in enumerate(lst):
		if isinstance(item,dict):
			tree[i]=treestr(Clict(item))
		else:
			tree[i]=repr(item)
	return tree






