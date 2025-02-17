class Clict(dict):
	__module__ = None
	__qualname__ = "Clict"
	__version__ = '0.6.1'

	def __new__(__c, *a, **k):
		# print('__new__ called with:' ,f'{k=}{v=}')
		return super().__new__(__c, *a, **k)

	def __init__(__s, *a, **k):
		super().__init__()
		if a:    __s.__args__(*a)
		if k:    __s.__kwargs__(**k)

	def __args__(__s, *a):
		for i, arg in enumerate(a):
			if isinstance(arg, dict):
				from Clict.from_other.types import fromDict
				dct = fromDict(arg)
				for key in dct:
					__s[key] = dct[key]
			elif isinstance(arg, list):
				from Clict.from_other.types import fromList

				dct = fromList(arg)
				for key in dct:
					__s[i][key] = dct[key]
			else:
				__s[i] = arg

	def __kwargs__(__s, **k):
		for key in k:
			if isinstance(k[key], dict):
				from Clict.from_other.types import fromDict
				__s[key] = fromDict(k[key])
			elif isinstance(k[key], list):
				from Clict.from_other.types import fromList
				__s[key] = fromList(k[key])
			else:
				__s[key] = k[key]

	def __setattr__(__s, k, v):
		# print('setattr_called with:' ,f'{k=}{v=}')
		k = __s.__expandkey__(k)
		__s[k] = v

	# super().__setitem__(k,v)

	def __getattr__(__s, k):
		# print('getattr_called with:', f'{k=}')
		k = __s.__expandkey__(k)
		return super().__getitem__(k)

	def __setitem__(__s, k, v):
		# print('setitem_called with:' ,f'{k=}{v=}')
		k = __s.__expandkey__(k)
		super().__setitem__(k, v)

	def __getitem__(__s, k, default=None):
		# print('getitem_called with:' ,f'{k=}')
		k = __s.__expandkey__(k)
		return super().__getitem__(k)

	def __get__(__s, k, default=None):
		# print('__get__ called with:' ,f'{k=}{default}')
		k = __s.__expandkey__(k)
		return super().__getitem__(k)

	def __dict__(__s):
		sdict = dict()
		for attr in super().keys():
			if isinstance(__s[attr], Clict):
				sdict[attr] = __s[attr].__dict__()
			else:
				sdict[attr] = __s[attr]

		return sdict
	def __missing__(__s, k):
		# print('missing called with:' ,f'{k=}')
		missing = Clict()
		__s.__setitem__(k, missing)
		return super().__getitem__(k)


	def __contains__(__s, item):

		return (item in __s.__dict__().keys())

	def __iter__(__s):
		return (i for i in __s.__clean__())

	def __hidden__(__s):
		hidden = Clict()
		pfx = __s.__pfx__()
		for key in [*super().__iter__()]:
			if str(key).startswith(pfx):
				nkey = str(key).removeprefix(pfx)
				nkey = str(nkey).removeprefix('_')
				hidden[nkey] = __s.__getitem__(key)
		return hidden



	def __clean__(__s):
		result = []
		for key in [*super().__iter__()]:
			if not str(key).startswith(__s.__pfx__()):
				result += [key]
		return result

	def __pfx__(__s):
		prefix = type(__s).__name__
		pfx = f'_{prefix}_'
		return pfx

	def __expandkey__(__s, k):

		if str(k).startswith('__'):
			pass
		elif str(k).startswith('_'):
			if ''.join(set(k) - set(',j.e')).isnumeric():
				k = k[1:]
			else:
				pfx = __s.__pfx__()
				if not str(k).startswith(pfx):
					k = f'{pfx}{k}'
		#
		# if isinstance(k,(int,float,complex)):
		# 	k=f'_{k}'
		return k

	def _get(__s, k, default=None):
		# print(f'get called with {k}')
		k = __s.__expandkey__(k)
		return super().get(k)

	def _keys(__s):
		return __s.__clean__()

	def _items(__s):
		Items = {}
		keys = __s.__clean__()
		for key in keys:
			Items[key] = super().__getitem__(key)
		return Items

	def _values(__s):
		Values = []
		keys = __s.__clean__()
		for key in keys:
			Values += [super().__getitem__(key)]
		return Values

	def __str__(__s):
		return  '\u007b' + ','.join([f"{str(x)}:{str(__s[x])}" for x in __s]) + '\u007d'

	def __repr__(__s, color=False):
		return __s.__str__()

	def __eq__(__s, other):
		eq=False
		if dict(__s)==other:
			eq=True
		return eq
	def template(__s):
		return Clict(__s)

