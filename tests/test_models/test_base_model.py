#!/usr/bin/python3
""" Test cases for the base model"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import json

class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

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

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_correct_output(self):
        created_at = datetime.today()
        bm = BaseModel()
        bm.id = "a572cae7-0dd3-4e1f-b353-9b43731c09ba"
        bm.created_at = created_at
        bm.updated_at = created_at
        expected = {
            'id': 'a572cae7-0dd3-4e1f-b353-9b43731c09ba',
            '__class__': 'BaseModel',
            'created_at': created_at.isoformat(),
            'updated_at': created_at.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), expected)

    def test_to_dict_contains_added_attributes(self):
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 98
        bm = obj.to_dict()
        self.assertIn("id", bm)
        self.assertIn("created_at", bm)
        self.assertIn("updated_at", bm)
        self.assertIn("__class__", bm)
        self.assertIn("name", bm)
        self.assertIn("my_number", bm)

    def test_create_with_kwargs(self):
        bm1 = BaseModel()
        bm2 = BaseModel(**bm1.to_dict())
        self.assertIsInstance(bm2, BaseModel)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

if __name__ == "__main__":
    unittest.main()
