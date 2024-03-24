#!/usr/bin/python3
""" Test cases for the base model"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """testing City class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = City({
        "state_id": "state_id",
        "name": "name"
        })

    def test_state_id(self):
        """ test state_id """
        self.assertEqual(self.new.state_id, "state_id")

    def test_name(self):
        """ test name """
        self.assertEqual(self.new.name, "name")
