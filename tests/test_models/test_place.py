#!/usr/bin/python3
""" Test cases for the base model"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing Place class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = Place()

    def test_city_id(self):
        """ test city_id """
        self.assertEqual(self.new.city_id, "")

    def test_user_id(self):
        """ test user_id """
        self.assertEqual(self.new.user_id, "")

    def test_name(self):
        """ test name """
        self.assertEqual(self.new.name, "")

    def test_description(self):
        """ test description """
        self.assertEqual(self.new.description, "")

    def test_number_rooms(self):
        """ test number_rooms """
        self.assertEqual(self.new.number_rooms, 0)

    def test_number_bathrooms(self):
        """ test number_bathrooms """
        self.assertEqual(self.new.number_bathrooms, 0)

    def test_max_guest(self):
        """ test max_guest """
        self.assertEqual(self.new.max_guest, 0)

    def test_price_by_night(self):
        """ test price_by_night """
        self.assertEqual(self.new.price_by_night, 0)

    def test_latitude(self):
        """ test latitude """
        self.assertEqual(self.new.latitude, 0.0)

    def test_longitude(self):
        """ test longitude """
        self.assertEqual(self.new.longitude, 0.0)

    def test_amenity_ids(self):
        """ test amenity_ids """
        self.assertEqual(self.new.amenity_ids, [])
