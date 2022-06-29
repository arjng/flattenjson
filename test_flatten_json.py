import unittest
import json
import flatten_json
from flatten_json import flatten, flatten_input
class TestJsonFlatten(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')
	def test_flatten_simple(self):
		self.assertEqual(flatten({'a': 1}), {"a": 1})
	def test_flatten_empty(self):
		self.assertEqual(flatten({}), {})
	def test_flatten_two_level(self):
		input = {"a": 1, "b": True, "c": {"d": 3, "e": "test"}}
		output = {"a": 1, "b": True, "c.d": 3, "c.e": "test"}
		self.assertEqual(flatten(input), output)
	def test_flatten_multi_level(self):
		input = {
		    "a": 1,
		    "b": True,
		    "c": {
		        "d": 3,
		        "e": "test",
		        "f": {"x": "fast", "y": 3, "c": {"d": False}, "e": 2},
		        "g": {"1": 3, "2": True},
		        "h": 2,
		    },
		    "y": "x",
		}
		output = {
		    "a": 1,
		    "b": True,
		    "c.d": 3,
		    "c.e": "test",
		    "c.f.x": "fast",
		    "c.f.y": 3,
		    "c.f.c.d": False,
		    "c.f.e": 2,
		    "c.g.1": 3,
		    "c.g.2": True,
		    "c.h": 2,
		    "y": "x",
		}
		self.assertEqual(flatten(input), output)
	def test_invalid_input(self):
		self.assertRaises(json.decoder.JSONDecodeError, flatten_input, '{"a": ')
	def test_flatten_input(self):
		input = '{"a": 1, "b": true, "c": {"d": 3, "e": "test"}}'
		output = '{"a": 1, "b": true, "c.d": 3, "c.e": "test"}'
		self.assertEqual(flatten_input(input), output)



