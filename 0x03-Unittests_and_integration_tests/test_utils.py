#!/usr/bin/env python3
"""Display utils.access_nested_map function"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Initialize testing access"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({"a": 1}, ("b",), KeyError),
        ({"a": {"b": 2}}, ("a", "c"), KeyError),
        ({}, ("a",), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

