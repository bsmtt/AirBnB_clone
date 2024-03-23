#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the FileStorage method """

    def test_all(self):
        """ __objects is properly returned """
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_new(self):
        """ New object is correctly added to storage """
        new = BaseModel()
        temp = {}
        temp.update(storage.all())
        self.assertTrue(temp[new.to_dict()['__class__'] + '.' + new.id] is dict)

    def test_save(self):
        """ storage save to json file """
        new = BaseModel() 
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload(self):
        """ test reload __object in storage """
        new = BaseModel() 
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])
