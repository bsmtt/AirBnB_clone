#!/usr/bin/python3
"""module defines a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class a class User that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """ user class constructor """
        for key , value in kwargs.items():
            if key == "email":
                self.email = value
            if key == "password":
                self.password = value
            if key == "first_name":
                self.first_name = value
            if key == "last_name":
                self.last_name = value
        super().__init__(*args, **kwargs)
