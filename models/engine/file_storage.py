#!/usr/bin/python3
"""

"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review



class FileStorage:
    """ """

    __file__path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        main_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({main_key: obj})

    def save(self):
        newdict = {}
        with open(self.__file__path, 'w', encoding="UTF-8") as filejson:
            for key, value in self.__objects.items():
                newdict[key] = value.to_dict()
            #json.dump(newdict, filejson)
            filejson.write(json.dumps(newdict))

    def reload(self):
        try:
            with open(self.__file__path, 'r', encoding='UTF-8') as file:
                text = file.read()
                if (len(text) > 0):
                    dicty = json.loads(text)
                    for key, value in dicty.items():
                        x = eval(value["__class__"])(**value)
                        self.__objects[key] = x
        except:
            pass
