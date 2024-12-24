#!/usr/bin/env python

from Clict.Typedef import ClictBase
from Clict.structs import Self




class Clict(ClictBase):
	__module__ = None
	__qualname__ = "Clict"
	__version__ = '0.6.1'
	
	def __init__(__s, *a, **k):
		if a:  __s.__args__(*a)
		if k:  __s.__kwargs__(**k)
		super().__init__()
	def values(__s):
		return super()._values()
	
	def keys(__s):
		return super()._keys()
	def items(__s):
		return super()._items()
