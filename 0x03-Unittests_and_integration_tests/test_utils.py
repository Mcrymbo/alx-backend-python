#!/usr/bin/env python3
"""
Tests utils class
"""
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests access_nested_map from utils module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """
        method that tests acess_nested_map
        """
        output = access_nested_map(map, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """ raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(output, e.exception)


class TestGetJson(unittest.TestCase):
    """
    Implememnts test cases for get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test get_json method
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    test memoize class
    """

    class TestClass:
        """ test class """
        def a_method(self):
            """ returns 42 always """
            return 42

        @memoize
        def a_property(self):
            """ returns memoize property """
            return self.a_method()

    with patch.object(TestClass, 'a_method', return_value=42) as fun:
        test = TestClass()
        test.a_property
        test.a_property
        fun.asset_called_once()
