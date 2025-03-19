

from Clict.ClictBase.base import Clict as ClictBase
class Self(ClictBase):
	node:dict
	name:str
	parent:dict
	root:dict
	path:list

	def __init__(__s,*a,**k):
		super().init()
		__s.node=k.get('node')
		__s.name= k.get('name')
		__s.parent=k.get('parent')
		__s.root=k.get('root')
		__s.path=k.get('path')
		__s.__root__()
		__s.__pathlist__()


	def __parent__(s,parent):
		if parent is not None:
			s.parent=parent
			s.root=s.parent.__getSelf__().root

	def __root__(s):
		if s.parent is None:
			s.root=s.node
			s.path=[s.root,]

	def __pathlist__(s):
		if s.parent is not None:
			s.path = [*s.parent.__getSelf__().path,s.node]




