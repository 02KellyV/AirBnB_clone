#!/usr/bin/python3
""" Unittests Amenity obj Module"""

import unittest
from models import storage
from models.amenity import Amenity
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test Amenity obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/amenity.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = Amenity()
        self.asserIsInstance(a, Amenity)

    def test_assert_is_subclass(self):
        """ Test amenity is subclss BaseM """
        a = Amenity()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test amenity have args"""
        a = Amenity(8)
        self.assertEqual(type(a).__name__, "Amenity")
        self.assertFalse(hasattr(a, "8"))

if __name__ == "__main__":
    unittest.main()
