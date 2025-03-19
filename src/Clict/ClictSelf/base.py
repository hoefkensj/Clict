
from Clict.ClictBase.base  import Clict as clictbase
from Clict.ClictSelf.support import Opts,Prop

class Self(clictbase):
	_self:clictbase
	_path:list
	name:str
	parent:clictbase
	root:clictbase
	opts:Opts
	prop:Prop

	def __init__(__s,*a,**k):
		__s._obj=k.get('obj')
		__s._args=k.get('args')
		__s._kwargs=k.get('kwargs')
		__s.name= k.get('name')
		__s.__parent__(k.get('parent'))
		__s.__root__()
		__s._path=[__s.name,'self']
	def __parent__(s,parent):
		s.parent=parent
		if parent is not None:
			s.root=s.parent._self.root
			s.opts=s.parent._self.opts
			s.prop=s.parent._self.prop


	def __root__(s):
		if s.parent is None:
			s.root=s._self
			s.opts=Opts()
			s.prop=Prop()




