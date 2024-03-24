#!/usr/bin/python3
""" Test cases for the base model"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing User class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = User({
        "email": "email",
        "password": "password",
        "first_name": "first_name",
        "last_name": "last_name"
        })

    def test_email(self):
        """ test email """
        self.assertEqual(self.new.email, "email")

    def test_password(self):
        """ test password """
        self.assertEqual(self.new.password, "password")

    def test_first_name(self):
        """ test first name """
        self.assertEqual(self.new.first_name, "first_name")

    def test_last_name(self):
        """ test last name """
        self.assertEqual(self.new.last_name, "last_name")
