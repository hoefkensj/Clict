#!/usr/bin/env python
import unittest
from Clict import Clict


class TestClict(unittest.TestCase):

	def test_init_with_dict(s):
		c = Clict(a=1, b=2)
		s.assertEqual(c['a'], 1)
		s.assertEqual(c['b'], 2)

	def test_set_get_item(s):
		c = Clict()
		c['a'] = 1
		s.assertEqual(c['a'], 1)

	def test_set_get_attr(s):
		c = Clict()
		c.a = 1
		s.assertEqual(c.a, 1)

	def test_missing_key(s):
		c = Clict()
		s.assertIsInstance(c['missing'], Clict)

	def test_contains_key(s):
		c = Clict(a=1)
		s.assertIn('a', c)
		s.assertNotIn('b', c)

	def test_keys(s):
		c = Clict(a=1, b=2)
		s.assertListEqual(list(c.keys()), ['a', 'b'])

	def test_items(s):
		c = Clict(a=1, b=2)
		s.assertDictEqual(c.items(), {'a': 1, 'b': 2})

	def test_values(s):
		c = Clict(a=1, b=2)
		s.assertListEqual(c.values(), [1, 2])

	def test_set_parent(s):
		c = Clict()
		c.d.asplit.child='findme'
		c.d.bsplit.child='fromhere'
		# localparent=c.d.__setparent__('iamparent')
		s.assertEqual(c.d.bsplit.__getparent__()().asplit.child,'findme')

	def test_str(s):
		c = Clict(a=1, b=2)
		s.assertIsInstance(str(c), str)

	def test_fancy_str(s):
		c = Clict(a=1, b=2)
		c.__setstrstyle__('fancy')
		s.assertIsInstance(c.__str__(), str)

	def test_convert(s):
		c = Clict()
		c.__convert__({'a': {'b': 2}})
		s.assertIsInstance(c['a'], Clict)
		s.assertEqual(c['a']['b'], 2)


if __name__ == '__main__':
	unittest.main()
