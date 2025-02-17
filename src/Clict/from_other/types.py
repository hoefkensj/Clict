from Clict.Clict import Clict
def fromDict(data):
	__s=Clict()
	for key in data:
		if isinstance(data[key],dict):
			__s[key]=fromDict(data[key])
		elif isinstance(data[key],list):
			__s[key]=fromList(data[key])
		else:
			__s[key]=data[key]
	return __s

def fromList(data):
	__s=Clict()
	for i,item in enumerate(data):
		if isinstance(item,dict):
			__s[i]=fromDict(item)
		elif isinstance(data[i],list):
			__s[i]=fromList(*item)
		else:
			__s[i]=item
	return __s

