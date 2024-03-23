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
        print(kwargs)
        """ """
        super().__init__(*args, **kwargs)
