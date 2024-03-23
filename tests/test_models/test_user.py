#!/usr/bin/python3
""" Test cases for the base model"""

import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """testing User class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.user = User({
        "email": "email",
        "password": "password",
        "first_name": "first_name",
        "last_name": "last_name"
        })

    def test_email(self):
        """ test email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test password """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_first_name(self):
        """ test first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)
