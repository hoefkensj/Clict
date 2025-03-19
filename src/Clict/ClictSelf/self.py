from  Clict.ClictSelf.base import Self as SelfBase
class Self(SelfBase):



	def __init__(__s,*a,**k):
		super().__init__()


	def __missing__(s):
		breakpoint()
		return super().__getitem__(k)

