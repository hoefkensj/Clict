#!/usr/bin/env python
import unittest
import src
from Clict.typedef import Clict
import QDPrintTree
from QDPrintTree import pTree




class MyTestCase(unittest.TestCase):

	def test_clict_instances(s):
		def eprint(a):
			print(a)

		def autotest(tests):
			test, run=tests

			nonlocal s
			print('--------------')
			for r,t in zip(run,test):
				print(t)
				if r==pTree:
					r(eval(t))
				elif r==eprint:
					exec(t)
					rr=eval(t)
					eprint(rr)
				elif r==print:
					pass
				else:
					result=r(t)
					if result is not None:
						print(eval(result))

		a = Clict()
		a.b.c.d.e.f = 'test'
		a.b.c.d.e.g = 'ikkel'
		a.b.c.k.e.g = 'ikkel'
		a.b.c.d.e.j = {'h': 'i'}
		a.__ishidden__ = 'secret'
		print(a)
		print(a.__ishidden__)
		print(a.b.c.__parent__)
		print(a.b.c.d.__parent__.keys())



if __name__ == '__main__':
	unittest.main()
