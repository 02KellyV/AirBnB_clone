#!/usr/bin/python3
"""
This contains a base class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A BaseModel class"""
    def __init__(self):
        """Initialize class base"""
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """"""
        return ("[{}] {} {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary """
        newBase = self.__dict__.copy()
        newBase["__class__"] = self.__class__.__name__
        newBase["create_at"] = self.create_at
        newBase["update_at"] = self.update_at
        return newBase
