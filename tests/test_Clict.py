#!/usr/bin/env python
import unittest
import src
import QDPrintTree
from QDPrintTree import pTree



class MyTestCase(unittest.TestCase):

	def test_clict_instances(s):
		from Clict import Clict
		tmpa=Clict()
		s.assertIsInstance(tmpa,Clict)
		tmpb=Clict()
		tmpb.b='string'
		print(type(tmpb))
		print(type(tmpb.b))
		s.assertIsInstance(tmpb,Clict)
		s.assertIsInstance(tmpb.b,str)
		print('-----')
		tmpb=Clict()
		print(type(tmpb))
		s.assertIsInstance(tmpb,Clict)
		print('-----')

		tmpb.b='string'
		print(type(tmpb.b))

		s.assertIsInstance(tmpb.b,str)
		print('-----')
		tmpb.c.d={'f':'g'}
		print(type(tmpb.c))
		print('-----')

		s.assertIsInstance(tmpb.c,Clict)
		print(type(tmpb.c.d))
		s.assertIsInstance(tmpb.c.d,dict)
		print(type(tmpb.c.d['f']))
		s.assertIsInstance(tmpb.c.d['f'],str)
		print(tmpb.c.d['f'])
		print(tmpb)

		tmpc=Clict()
		print(type(tmpc.d))
		print(type(tmpc.d['e']))
		print(type(tmpc.d.e))
		print(type(tmpc.d.f))
		print(tmpc)
		a=Clict()
		a.b.c.d.e.f.g.h.i.j.k.l.m.n='test'
		print(a)

