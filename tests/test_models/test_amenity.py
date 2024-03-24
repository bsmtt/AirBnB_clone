#!/usr/bin/python3
""" Test cases for the base model"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing Amenity class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = Amenity({"name": "name"})

    def test_name(self):
        """ test name """
        self.assertEqual(self.new.email, "email")
