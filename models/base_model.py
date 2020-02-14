#!/usr/bin/python3
"""
This contains a base class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    created_at = datetime.now()
    updated_at = datetime.now()

    """A BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialize class base"""
        self.id = str(uuid4())
        if kwargs is not None:
            for keys, value in kwargs.items():
                if keys is not "__class__":
                    if keys is "created_at" or keys is "updated_at":
                        value = datetime.strptime(self.created_at.isoformat(), "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary """
        newbase = self.__dict__.copy()
        newbase.update({"__class__": self.__class__.__name__})
        newbase.update({"created_at": self.created_at.isoformat()})
        newbase.update({"updated_at": self.updated_at})
        return newbase
