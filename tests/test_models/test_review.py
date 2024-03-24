#!/usr/bin/python3
""" Test cases for the base model"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """testing Review class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = Review({
            "place_id": "place_id",
            "user_id": "user_id",
            "text": "text"
            })

    def test_place_id(self):
        """ test place_id """
        self.assertEqual(self.new.place_id, "place_id")

    def test_user_id(self):
        """ test user_id """
        self.assertEqual(self.new.user_id, "user_id")

    def test_text(self):
        """ text first name """
        self.assertEqual(self.new.text, "text")
