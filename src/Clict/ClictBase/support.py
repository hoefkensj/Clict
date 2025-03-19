from Clict.ClictBase.base  import Clict as clictbase
from enum import Enum,StrEnum
from dataclasses import dataclass,field
from collections import namedtuple
import re




class TemplateString(str):
	def format(s,**k):
		def substitute(match):
			key = match.group(1)
			if key in k:
				return str(k[key])
			return match.group(0)  # Keep it unchanged if not in mapping

		template=s.__str__()
		prev = None
		while prev != template :  # Stop when no further changes occur
			prev = template
			template = re.sub(r'\{([^{}]+)\}', substitute, template)
		return template
