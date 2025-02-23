from configparser import ConfigParser,ExtendedInterpolation

def Parser():
	opts = {'delimiters': (':', '='), 'allow_no_value': True, 'strict': False}
	parser = ConfigParser(interpolation=ExtendedInterpolation(), **opts)
	parser.optionxform = lambda option: option
	return parser

P=Parser()
P.read('dwagent.service')
print(P.sections())