#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
        Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF to exit the program."""
        return True

    def do_quit(self, line):
        """Quit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
