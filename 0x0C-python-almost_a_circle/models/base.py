"""Base model module"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        self.id = id if id is not None else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert to JSON string"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        """Convert to list of dictionaries"""
        return json.loads(json_string) if json_string\
            and json_string != "[]" else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
        filename = "{}.json".format(cls.__name__)
        lst = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, "w") as file:
            file.write(cls.to_json_string(lst))

    @classmethod
    def create(cls, **dic):
        """Create instance from dictionary"""
        new = cls(1) if cls.__name__ == "Square" else cls(1, 1)
        new.update(**dic)
        return new

    @classmethod
    def load_from_file(cls):
        """Load list of instances from file"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                lst_item = file.read()
        except FileNotFoundError:
            return []
        lst_dic = cls.from_json_string(lst_item)
        return [cls.create(**ele) for ele in lst_dic]
