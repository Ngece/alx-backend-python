#!/usr/bin/env python3
"""Unit tests for utils.py file"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from utils import AsyncMock, async_call

class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map function"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(error.exception)) 

class TestGetJson(unittest.TestCase):
    """TestGetJson Class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    @patch('test_utils.get_json')

    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        mock_get.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """TestMemoize Class"""
    def test_memoize(self):
        """Test memoize function"""
        class TestClass:
            """TestClass Class"""
            def a_method(self):
                """a_method method"""
                return 42

            @memoize
            def a_property(self):
                """a_property method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, mock_method.return_value)
            self.assertEqual(test.a_property, mock_method.return_value)
            mock_method.assert_called_once()

class TestAsyncMock(unittest.TestCase):
    """TestAsyncMock Class"""
    def test_async_mock(self):
        """Test async_mock function"""
        am = AsyncMock()
        self.assertEqual(asyncio.iscoroutinefunction(type(am)), True)
        self.assertEqual(asyncio.iscoroutinefunction(type(am.return_value)), True)

class TestAsyncCall(unittest.TestCase):
    """TestAsyncCall Class"""
    @patch('test_utils.async_call')
    
    def test_async_call(self, mock_async):
        """Test async_call function"""
        mock_async.return_value = 'test'
        self.assertEqual(async_call(), 'test')
        mock_async.assert_called_once()

if __name__ == '__main__':
    unittest.main()