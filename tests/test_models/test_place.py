#!/usr/bin/python3
""" Unittests Place obj Module"""

import unittest
from models import storage
from models.place import Place
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test Place obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/place.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = Place()
        self.asserIsInstance(a, Place)

    def test_assert_is_subclass(self):
        """ Test place is subclss BaseM """
        a = Place()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test place have args"""
        a = Place(8)
        self.assertEqual(type(a).__name__, "Place")
        self.assertFalse(hasattr(a, "8"))


if __name__ == "__main__":
    unittest.main()
