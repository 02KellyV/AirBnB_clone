#!/usr/bin/python3
""" Unittests City obj Module"""

import unittest
from models import storage
from models.city import City
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test City obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/city.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = City()
        self.asserIsInstance(a, City)

    def test_assert_is_subclass(self):
        """ Test city is subclss BaseM """
        a = City()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test city have args"""
        a = City(8)
        self.assertEqual(type(a).__name__, "City")
        self.assertFalse(hasattr(a, "8"))


if __name__ == "__main__":
    unittest.main()
