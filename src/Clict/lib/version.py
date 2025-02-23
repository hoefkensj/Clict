
#!/usr/bin/env python

def n0(x):	return int((0*(x<0))+(x*(x>0)))

class Version():
	def __init__(__s,major=0,minor=0,patch=0,release=None):
		T=tuple(n0(major),n0(minor),n0(patch))
		E=[1e6,1e3,1e0]
		U=['M','m','p']
		I=['M','K','E']
		__s.e=E
		__s.int=int((T[0]*E[0])+(T[1]*E[1])+(T[2]*E[2]))
		__s.major=T[0]
		__s.minor=T[1]
		__s.patch=T[2]
		__s.tuple=T
		__s.release=release
		__s.version=None
		__s.validate()
	def validate(__s):
		if sum(__s.tuple) == 0:
			__s.bump()


		pass
	major = property(lambda __s: 0)
	"""the major(1st) part of a version number

	:type: int
	"""

	minor = property(lambda self: 0)
	"""the minor(2nd) part of a version number (optional)
 
	:type: int
	"""

	patch = property(lambda self: 0)
	"""the patch(3rd) part of a version  number (optional)

	:type: int
	"""

	release = property(lambda self: '')
	"""the release(4th) part of a version number (optional)

	:type: str
	"""
