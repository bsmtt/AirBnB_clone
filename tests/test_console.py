#!/usr/bin/python3
"""Defines unittests for console.py.
"""

import unittest
from models import storage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def test_change_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_handle_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual("Quit the program.", output.getvalue().strip())

    def test_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            msg = "** class name missing **"
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_doesnot_exist_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create New"))
            self.assertEqual(
                "** class doesn't exist **",
                output.getvalue().strip()
            )

    def test_nnknown_syntax(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("test"))
            self.assertEqual(
                "*** Unknown syntax: test",
                output.getvalue().strip()
            )


if __name__ == "__main__":
    unittest.main()
