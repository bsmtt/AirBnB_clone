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
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ test reload __object in storage """
        storage.reload()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
