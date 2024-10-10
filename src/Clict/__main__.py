#!/usr/bin/env python
import Clict
import click as C
from pathlib import Path
from Clict import from_Config


class DefaultCommandGroup(C.Group):
	def resolve_command(self, ctx, args):
		args.append("show")
		return super().resolve_command(ctx, args)





@C.command()
@C.argument('path', default='.')
@C.pass_context
def cmd_from_config(ctx,path):
	"""help from config"""
	p=Path(path).resolve()
	ctx.obj.path=p
	if p.exists():
		ctx.obj.data=from_Config(p)
	print(repr(ctx.obj.data))



@C.group()
@C.pass_context
def grp_from(ctx):
	"""help from"""
	pass

@C.group()
@C.pass_context
def grp_cli(ctx):
	"""	help cli"""
	ctx.ensure_object(Clict.Clict)



grp_from.add_command(cmd_from_config, name='config')
grp_cli.add_command(grp_from,name='show')
grp_cli.add_command(grp_from,name='from')



if __name__ == '__main__':
	grp_cli()
