#!/usr/bin/env python
from Clict.Typedef import ClictBase

self=ClictBase()
self.name=None
self.parent=None
self.path=None


stat=ClictBase()
stat.is_real=None
stat.is_virt=None
stat.is_file=None
stat.is_folder=None
stat.is_config=None


opts=ClictBase()
opts.str_color=None
opts.str_multi=None
opts.rep_tree=None
opts.rep_color=None

