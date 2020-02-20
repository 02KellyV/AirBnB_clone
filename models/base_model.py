from uuid import uuid4
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize class base"""
        if kwargs:
            for keys, value in kwargs.items():
                if keys != "__class__":
                    if keys == "created_at" or keys == "updated_at":
                        value = datetime.strptime(value, time)
                    setattr(self, keys, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """print the class name, id and directory"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary """
        newbase = self.__dict__.copy()
        newbase["__class__"] = self.__class__.__name__
        newbase["created_at"] = self.created_at.isoformat()
        newbase["updated_at"] = self.updated_at.isoformat()
        return newbase
