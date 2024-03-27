#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
        Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }
    dot_cmds = [
        'all',
        'count',
        'show',
        'destroy',
        'update'
        ]

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] is '{' and pline[-1] is'}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

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
            print(["{}".format(str(val)) for val in storage.all().items()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for val in storage.all().values():
                if args[0] == val.__class__.__name__:
                    obj.append(val.__str__())
            print(obj)

    def do_update(self, line):
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
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
        else:
            obj = stored_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
