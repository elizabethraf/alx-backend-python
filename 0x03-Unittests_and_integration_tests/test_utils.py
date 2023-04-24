#!/usr/bin/env python3
"""Display utils.access_nested_map function"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)
import requests


Class TestAccessNestedMap(unittest.TestCase):
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
    def test_access_nested_map_exception(self, nested_map, path):
        """Testing Errors"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


Class TestGetJson(unittest.TestCase):
    """Initialise Testcase"""
    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, mock_get, test_url, test_payload):
        """Return the expected payload"""
        mock_json = Mock(return_value=test_payload)
        mock_get.return_value = Mock(json=mock_json)

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        class Mocked(Mock):
            """Define Class"""

            def json(self):
                """Initialize json"""

                return payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


Class TestMemoize(unittest.TestCase):
    """Ininitialize unittest"""

    def test_memoize(self):
        """Initialize test"""

        class TestClass:
            """Define class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
