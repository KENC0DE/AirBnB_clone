#!/usr/bin/python3
"""
### Data Storage File ###
"""


import json
import os
import datetime


class FileStorage:
    """
    Storage Class.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return saved Objects """
        return self.__objects

    def new(self, obj):
        """ Store passed objects in dict """
        key = str(obj.__class__.__name__ + "." + obj.id)
        new_obj = {key: obj}
        self.__objects.update(new_obj)

    def save(self):
        """ Serialize objects to a json file."""
        with open(self.__file_path, "w") as file:
            save_file = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(save_file, file)

    def reload(self):
        """ Loads saved Json file """
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(self.__file_path, "r", encoding='utf-8') as file:
            obj_dict = json.load(file)
            FileStorage.__objects = {key: self.load_class(val['__class__'])
                                     (**val) for key, val in obj_dict.items()}

    def load_class(self, name):
        """ Creates class Refrence """
        from models.base_model import BaseModel
        from models.user import User

        classes = {
            "BaseModel": BaseModel,
            "User": User
        }
        if name is None:
            return classes

        if name not in classes:
            return None

        return classes[name]

    def attrib(self, name):
        """Returns the valid attributes"""
        attributes = {
            "id": str,
            "created_at": datetime.datetime,
            "updated_at": datetime.datetime,
            "email": str,
            "password": str,
            "first_name": str,
            "last_name": str,
            "name": str,
            "state_id": str,
            "city_id": str,
            "user_id": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list,
            "place_id": str,
            "user_id": str,
            "text": str
        }
        return attributes[name]
