#!/usr/bin/python3
"""the Base Model """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """the BaseModel of HBnB """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel."""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

        storage.new(self)

    def __str__(self):
        """ string representation of the class. """
        self_name = type(self).__name__
        return "[{}] ({}) {}".format(self_name, self.id, self.__dict__)

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
