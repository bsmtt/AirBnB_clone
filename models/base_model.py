#!/usr/bin/python3
"""the Base Model """
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """the BaseModel of HBnB """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel."""
        print(kwargs)
        if not kwargs:
            print("============= no kwargs")
        else:
            print("============== kwargs")

        for k, v in kwargs.items():
            self.__dict__[k] = v

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        storage.new(self)

    def __str__(self):
        """ string representation of the class. """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)

    def save(self):
        """ save to instance. """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values """

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__

        return dict_copy
