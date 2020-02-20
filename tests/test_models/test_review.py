#!/usr/bin/python3
""" Unittests Review obj Module"""

import unittest
from models import storage
from models.review import Review
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test Review obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/review.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(Review.__doc__) > 1)
        self.assertTrue(len(Review.__init__.__doc__) > 1)
        self.assertTrue(len(Review.__str__.__doc__) > 1)
        self.assertTrue(len(Review.save.__doc__) > 1)
        self.assertTrue(len(Review.to_dict.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = Review()
        self.asserIsInstance(a, Review)

    def test_assert_is_subclass(self):
        """ Test review is subclss BaseM """
        a = Review()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test review have args"""
        a = Review(8)
        self.assertEqual(type(a).__name__, "Review")
        self.assertFalse(hasattr(a, "8"))

if __name__ == "__main__":
    unittest.main()
