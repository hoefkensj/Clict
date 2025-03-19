from Clict.ClictSelf.self import Self
from pathlib import Path


class ConfSelf(Self):
	def __init__(__s, *a, **k):
		__s.name = k.get('name')
		__s.parent = k.get('parent')
		__s.path = Path(k.get('path'))
		__s.file = k.get('file')
		__s.section = k.get('section')
		__s.key = k.get('key')
		__s.value = k.get('value')
		__s.strvalue = str(repr(__s.value))
		__s.types = None
		__s.type = None
		__s.parser = k.get('parser')
		__s.interpolation = None
		__s.stat = k.get('stat')
		__s.opts = k.get('opts')

		if __s.name is None:
			if __s.opts.flags.strip_file_Suffix:
				for suffix in __s.opts.include.file.suffix:
					__s.name = __s.path.name.removesuffix(suffix)
		__s.__types__()

	def __types__(__s):
		t = []
		t += ['folder'] * __s.stat.folder
		t += ['file'] * __s.stat.file
		t += ['section'] * __s.stat.section
		t += ['key'] * __s.stat.key

