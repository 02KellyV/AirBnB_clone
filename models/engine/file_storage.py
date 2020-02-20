#!/usr/bin/python3
""" File Storage Module"""

import json
import os.path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review


class FileStorage:
    """Class for Serializes and Deserializes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects, key classname.id val= obj"""
        main_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({main_key: obj})

    def save(self):
        """serializes __objects to JSON"""
        newdict = {}
        with open(self.__file_path, 'w', encoding="UTF-8") as filejson:
            for key, value in self.__objects.items():
                newdict[key] = value.to_dict()  # json.dump(newdict, filejson)
            filejson.write(json.dumps(newdict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as json_f:
                othrdict_objs = json.load(json_f)
            for key, val in othrdict_objs.items():
                self.__objects[key] = eval(val["__class__"])(**val)
