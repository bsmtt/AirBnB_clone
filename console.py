#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
        Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_EOF(self, line):
        """EOF to exit the program.
        """
        return True

    def do_quit(self, line):
        """Quit the program.
        """
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance of class
        Args:
            line: Arguments to enter with command: <class name>
        """

        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new = eval(args[0])()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Display the string repr of a class instance of a given id.
        """

        args = line.split(" ")
        stored_dict = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in stored_dict:
            print("** no instance found **")
        else:
            k = "{}.{}".format(args[0], args[1])
            val = stored_dict[k]
            print(val)

    def do_destroy(self, line):
        """destroy class instance of a given id.
        """

        args = line.split(" ")
        stored_dict = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in stored_dict:
            print("** no instance found **")
        else:
            k = "{}.{}".format(args[0], args[1])
            del stored_dict[k]
            storage.save()

    def do_all(self, line):
        """Display string representations of all instances
        """

        args = line.split(" ")
        if not line:
            print([val for val in storage.all().values()])
        else:
            obj = []
            for val in storage.all().values():
                if  args[0] == val.__class__.__name__:
                    obj.append(val.__str__())
            print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
