#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
worktime test suite

Default syntax:

./tests.py
    Run all unit tests
"""

__author__ = 'Victor Engmark'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__maintainer__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__license__ = 'GPL v3 or newer'

from doctest import testmod
import unittest

from worktime import worktime


class TestGenerator(unittest.TestCase):
    """Tests that generate output."""

    def test_no_options(self):
        """Use only default options."""
        self.assertNotEquals(
            worktime,
            '')


class TestDoc(unittest.TestCase):
    """Test Python documentation strings."""
    def test_doc(self):
        """Documentation tests."""
        self.assertEqual(testmod(worktime)[0], 0)


def main():
    """Run tests"""
    unittest.main()


if __name__ == '__main__':
    main()
