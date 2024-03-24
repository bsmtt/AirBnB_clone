#!/usr/bin/python3
""" Test cases for the base model"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """testing State class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.new = State()

    def test_name(self):
        """ test name """
        self.assertEqual(self.new.name, "")
