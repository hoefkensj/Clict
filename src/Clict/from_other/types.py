from Clict.ClictBase.base import Clict
def fromDict(data):
	__s=Clict()
	for key in data:
		if isinstance(data[key],Clict):
			__s[key]=data[key]
		if isinstance(data[key],dict):
			__s[key]=Clict(**data[key])

		elif isinstance(data[key],list):
			__s[key]=Clict(*data[key])
		else:
			__s[key]=data[key]
	return __s

def fromList(data):
	__s=Clict()
	for i,item in enumerate(data):
		if isinstance(item,dict):
			__s[i]=Clict(item)
		elif isinstance(data[i],list):
			__s[i]=fromList(*item)
		else:
			__s[i]=item
	return __s

