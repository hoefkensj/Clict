from Clict.base.Clict  import Clict as clictbase


class Opts(clictbase):
	def __init__(s,*a,**k):
		s.str.color=True
		s.str.tree=False
		s.repr.color=True
		s.repr.tree=True
		s.repr.braces.replace=lambda string : string.replace('{','[CLICT_REPL_U007B]').replace('}','[CLICT_REPL_U007D]')
		s.repr.braces.restore=lambda string : string.replace('[CLICT_REPL_U007B]','{').replace('[CLICT_REPL_U007D]','}')

		s.repr.colors.tree.rgb={
			'CLRTREE':'\x1b[38;2;96;96;96m',
			'CLRKEY':'\x1b[1;38;2;128;192;255m',
			'CLRSEP':'\x1b[1;38;2;255;255;255m',
			'CLRVAL':'\x1b[3;38;2;255;255;96m',
			'CLRCALL':'\x1b[3;38;2;255;32;32m',
			'RESET':'\x1b[m',
		}
		s.repr.colors.tree.bw = {
			'CLRTREE': '',
			'CLRKEY': '',
			'CLRSEP': '',
			'CLRVAL': '',
			'CLRCALL': '',
			'RESET': ''}
		s.repr.colors.tree.tpl={
			'CLRTREE': '{CLRTREE}',
			'CLRKEY'   : '{CLRKEY}',
			'CLRSEP': '{CLRSEP}',
			'CLRVAL'   : '{CLRVAL}',
			'CLRCALL'  : '{CLRCALL}',
			'RESET' : '{RESET}',
		}
		s.repr.symbols.tree.lastnode='┗━━━┳━╼'
		s.repr.symbols.tree.clictnode='┣━━━┳━╼ '
		s.repr.symbols.tree.parent='┃'
		s.repr.symbols.tree.replace='┳', '━'


class Self(clictbase):
	def __init__(__s,*a,**k):
		__s.name= k.get('name')
		__s.opts=Opts(k.get('opts'))
		__s.parent=k.get('parent')


