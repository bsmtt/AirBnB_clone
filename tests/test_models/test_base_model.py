#!/usr/bin/python3
""" Test cases for the base model"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def setUp(self):
        """
        testing
        """
        pass

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_two_models_diff_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
    
