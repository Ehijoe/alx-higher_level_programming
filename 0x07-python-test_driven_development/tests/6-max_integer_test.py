#!/usr/bin/python3
"""Test suite for max_integer function."""
from unittest import TestCase


class MaxIntegerTests(TestCase):
    """Test case for the max_integer function."""

    def setUp(self):
        """Set up each testcase."""
        self.max_integer = __import__('6-max_integer').max_integer

    def test_sorted_list(self):
        """Test for a list sorted in ascending order."""
        self.assertEqual(self.max_integer([1, 2, 3]), 3)

    def test_reversed_list(self):
        """Test for a list sorted in descending order."""
        self.assertEqual(self.max_integer([3, 2, 1]), 3)

    def test_unordered_list(self):
        """Test for an unsorted list."""
        self.assertEqual(self.max_integer([3, 6, 2, 7, 5]), 7)

    def test_empty_list(self):
        """Test for an empty list."""
        self.assertIs(self.max_integer(), None)
        self.assertIs(self.max_integer([]), None)

    def test_invalid_arg_type(self):
        """Test for an invalid argument type."""
        self.assertRaises(TypeError, self.max_integer, 4)
        self.assertRaises(TypeError, self.max_integer, 4.56)

    def test_tuple(self):
        """Test for a tuple."""
        self.assertEqual(self.max_integer((1, 4, 7, 5)), 7)
        self.assertEqual(self.max_integer((7, 5, 4, 1)), 7)
        self.assertEqual(self.max_integer((1, 4, 5, 7)), 7)

    def test_single_item(self):
        """Test for a list with only one item."""
        self.assertEqual(self.max_integer([0]), 0)
        self.assertEqual(self.max_integer([6]), 6)
        self.assertEqual(self.max_integer([-1]), -1)

    def test_negative_integers(self):
        """Test for lists with negative integers."""
        self.assertEqual(self.max_integer([-13, -5, -10, -31]), -5)
        self.assertEqual(self.max_integer([13, -5, 10, -31]), 13)

    def test_list_types(self):
        """Test for lists with incompatible element types."""
        self.assertRaises(TypeError, self.max_integer, [1, '3', 7])
        self.assertRaises(TypeError, self.max_integer, [1.0, '3', 7])
        self.assertRaises(TypeError, self.max_integer, [1, (1, 2), 7])
