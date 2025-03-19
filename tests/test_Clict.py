#!/usr/bin/env python
import unittest
from Clict import Clict
CA=None
CB = None
CZ = None

def makedata():
	global CA
	global CB
	global CZ
	CA = Clict(a=1, b=2)
	CB = Clict()
	CB['a'] = 1
	CB.b = 2
	CZ = Clict()
	
	
	
	
class TestClict(unittest.TestCase):
	

	
	def test_set_get(t):
		makedata()

		t.assertEqual(CA,CB)

		t.assertEqual(CA['a'], 1)
		t.assertEqual(CB['b'], 2)
		t.assertEqual(CB.a, 1)
		t.assertEqual(CA.b, 2)

		t.assertIn('a', CB)
		t.assertNotIn('d', CA)
		t.assertListEqual(['a', 'b'],list(CB.keys()))
		t.assertListEqual(['a', 'b'],list(CA.keys()))
		t.assertDictEqual( {'a': 1, 'b': 2},CA.items())
		t.assertListEqual(CB.values(), [1, 2])
		
	def test_missing(t):
		makedata()
		t.assertIsInstance(CZ.missing, dict)
	
	def test_set_parent(s):
		c = Clict()
		c.d.asplit.child.str='findme'
		c.d.bsplit.child.str='fromhere'
		# localparent=c.d.__setparent__('iamparent')

		s.assertEqual('fromhere',c.d.bsplit.child.str)
		s.assertEqual('findme',c.d.bsplit.child.getSelf().parent.getSelf().parent.asplit.child.str)

	# def test_str(s):
	# 	c = Clict(a=1, b=2)
	# 	s.assertIsInstance(str(c), str)
	#


	def test_fromdict(s):
		c = Clict({'a': {'b': 2}})
		s.assertIsInstance(c['a'], dict)
		s.assertEqual(c['a']['b'], 2)

	def test_fromlist(s):
		# breakpoint()
		c = Clict('a','b')
		# print(repr(c))
		s.assertEqual( 'a',c[0])
		s.assertEqual(c[1], 'b')
		c=Clict(['a','b'])
		# print(repr(c))
		s.assertEqual('a',c[0][0] )
		d=dict(c)
		s.assertEqual(c[0][1], 'b')

		# s.assertEqual(c._0._1, 'b')
		c=Clict(mylist=['a','b','c'])
		s.assertEqual('a',c.mylist[0] )
		c.mylist[2]='c'
		s.assertEqual(c.mylist[2], 'c')
	def test_printtree(s):
		c=Clict(['a','b'],g=['d',{'e':'f'}])
		c.p.q.r.s.t.u.v.w.x.y='test'*200
		c.p.q.r.s.t.u.v.w.x.a= print
		c.p.r.s.z=['i' for i in range(90)]
		print(repr(c))



if __name__ == '__main__':
	unittest.main()
