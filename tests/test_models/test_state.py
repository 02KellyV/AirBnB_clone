#!/usr/bin/python3
""" Unittests State obj Module"""

import unittest
from models import storage
from models.state import State
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test State obj Methods """

    def test_assert_stylepep8_amenity(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/state.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsamenity(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(State.__doc__) > 1)
        self.assertTrue(len(State.__init__.__doc__) > 1)
        self.assertTrue(len(State.__str__.__doc__) > 1)
        self.assertTrue(len(State.save.__doc__) > 1)
        self.assertTrue(len(State.to_dict.__doc__) > 1)

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = State()
        self.asserIsInstance(a, State)

    def test_assert_is_subclass(self):
        """ Test State is subclss BaseM """
        a = State()
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_assert_args(self):
        """Test State have args"""
        a = State(8)
        self.assertEqual(type(a).__name__, "State")
        self.assertFalse(hasattr(a, "8"))


if __name__ == "__main__":
    unittest.main()
