#!/usr/bin/env python
import unittest
import src
from src.Clict. import Clict



class MyTestCase(unittest.TestCase):

	def test_clict_instances(s):
		print(	'a=Clict()')
		a=Clict()
		print(a)
		b=Clict()
		d=Clict()
		a.a
		print(a)
		print(a.a)
		print(type(a))
		b['b']
		c=Clict({'c':Clict()})
		d.__d
		# s.assertIsInstance(a,Clict)
		print('a.a')
		s.assertIsInstance(a.a,Clict)
		s.assertIsInstance(a['a'],Clict)
		# s.assertIsInstance(a.get('a'),Clict)
		print('b.b')
		s.assertIsInstance(b.b,Clict)
		s.assertIsInstance(b['b'],Clict)
		# s.assertIsInstance(b.get('b'),Clict)
		print('c.c')
		s.assertIsInstance(c.c,Clict)
		s.assertIsInstance(c['c'],Clict)
		# s.assertIsInstance(c.get('c'),Clict)
		print('d.d')
		s.assertIsInstance(d.__d, Clict)
		s.assertIsInstance(d['__d'], Clict)
		# s.assertIsInstance(d.get('__d'), Clict)
		a.a.a
		b['b']['b']
		d.__d.__d
		print('a.a.a')
		s.assertIsInstance(a.a.a,Clict)
		s.assertIsInstance(a['a']['a'],Clict)
		# s.assertIsInstance(a.a.get('a'),Clict)
		print('b.b.b')

		s.assertIsInstance(b.b.b,Clict)
		s.assertIsInstance(b['b']['b'],Clict)
		# s.assertIsInstance(b.b.get('b'),Clict)
		p=Clict()
		p.__parents__('q.r.s.t.v.w')
		print(p)

# def test_Clict_Equals(s)	:
#
# 	s.assertEqual(a.b,a['b'])
# 	s.assertEqual(a.c,a['c'])
# 	s.assertIn('b', a.keys())
# 	s.assertNotIn('__hidden',a)
# 	s.assertEqual('secret',a.__hidden)
# 	print('__hidden' in a)
if __name__ == '__main__':
	unittest.main()
