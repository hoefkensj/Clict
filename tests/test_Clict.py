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
		tmpb=Clict()
		print(type(tmpb))
		s.assertIsInstance(tmpb,Clict)
		tmpb.b='string'
		print(type(tmpb.b))
		s.assertIsInstance(tmpb.b,str)
		tmpb.c.d={'f':'g'}
		print(type(tmpb.c))
		s.assertIsInstance(tmpb.c,Clict)
		print(type(tmpb.c.d))
		s.assertIsInstance(tmpb.c.d,dict)
		print(type(tmpb.c.d['f']))
		s.assertIsInstance(tmpb.c.d['f'],str)


