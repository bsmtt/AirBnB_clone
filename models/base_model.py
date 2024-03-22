#!/usr/bin/python3
"""the Base Model """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the BaseModel of HBnB """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel."""

        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if  k in ("updated_at", "created_at"):
                    self.__dict__[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """ string representation of the class. """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)

    def save(self):
        """ save to instance. """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ returns a dictionary containing all keys/values """

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__

        return dict_copy
