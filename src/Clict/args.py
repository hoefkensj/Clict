#!/usr/bin/env python
from Clict import Clict
class MakeOpts(Clict):
	def __init__(__s, opts=[],**k):
			super.__init__()
			__s.self.parent = lambda:
			__s.self.name = None
			__s.self.stem = None
			__s.self.suffix = None
			__s.self.cat = None


class Self(Clict):
	def __init__(__s,**k):
		opts=k.pop('opts',{})
		name=k.pop('n',k.pop('name','root'))
		parent=k.pop('P',k.pop('parent',None))
		super.__init__()
		__s.name=name
		__s.parent= lambda : parent
		__s.opts=




class keyword(Object):
	__module__ = None
	__qualname__ = "Clict_KeywordArgs"
	def __init__(__s,*a,**k):
		__s._self=
