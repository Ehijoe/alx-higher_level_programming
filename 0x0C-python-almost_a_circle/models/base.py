#!/usr/bin/python3
"""Base class."""
import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an object."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from a json string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file."""
        if list_objs is None:
            to_save = []
        else:
            to_save = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as output:
            output.write(Base.to_json_string(to_save))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of the class initialized with the dictionary."""
        obj = cls(2, 3)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def load_from_file(cls):
        """Return a list of objects loaded from a file."""
        obj_list = []
        with open(f"{cls.__name__}.json", "r", encoding="utf-8") as infile:
            obj_list = Base.from_json_string(infile.read())
        return [cls.create(**obj) for obj in obj_list]
