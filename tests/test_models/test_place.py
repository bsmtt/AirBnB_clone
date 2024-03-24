#!/usr/bin/python3
""" Test cases for the base model"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing Place class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = Place({
            "city_id": "city_id",
            "user_id": "user_id",
            "name": "name",
            "description": "description",
            "number_rooms": 0,
            "number_bathrooms": 0,
            "max_guest": 0,
            "price_by_night": 0,
            "latitude": 0.0,
            "longitude": 0.0,
            "amenity_ids": []
            })

    def test_city_id(self):
        """ test city_id """
        self.assertEqual(self.new.city_id, "city_id")

    def test_user_id(self):
        """ test user_id """
        self.assertEqual(self.new.user_id, "user_id")

    def test_name(self):
        """ test name """
        self.assertEqual(self.new.name, "name")

    def test_description(self):
        """ test description """
        self.assertEqual(self.new.description, "description")

    def test_number_rooms(self):
        """ test number_rooms """
        self.assertEqual(self.new.number_rooms, "number_rooms")

    def test_number_bathrooms(self):
        """ test number_bathrooms """
        self.assertEqual(self.new.number_bathrooms, "number_bathrooms")

    def test_max_guest(self):
        """ test max_guest """
        self.assertEqual(self.new.max_guest, "max_guest")

    def test_price_by_night(self):
        """ test price_by_night """
        self.assertEqual(self.new.price_by_night, "price_by_night")

    def test_latitude(self):
        """ test latitude """
        self.assertEqual(self.new.latitude, "latitude")

    def test_longitude(self):
        """ test longitude """
        self.assertEqual(self.new.longitude, "longitude")

    def test_amenity_ids(self):
        """ test amenity_ids """
        self.assertEqual(self.new.amenity_ids, "amenity_ids")
