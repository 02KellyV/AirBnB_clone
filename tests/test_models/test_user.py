#!/usr/bin/python3
""" Unittests User obj Module"""

import unittest
from models import storage
from models.user import User
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test User obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/user.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = User()
        self.asserIsInstance(a, User)

    def test_assert_is_subclass(self):
        """ Test User is subclss BaseM """
        a = User()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test User have args"""
        a = User(8)
        self.assertEqual(type(a).__name__, "User")
        self.assertFalse(hasattr(a, "8"))

if __name__ == "__main__":
    unittest.main()
