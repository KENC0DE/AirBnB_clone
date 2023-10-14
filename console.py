#!/usr/bin/python3
"""
### Command Interpreter ###
"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter Class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit Program """
        return True

    def do_EOF(self, arg):
        """ Quit Program """
        return True

    def do_create(self, arg):
        """ Create Object """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif storage.load_class(arg) is None:
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            arg = arg.split(' ')
            if storage.load_class(arg[0]) is None:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            arg = arg.split(' ')
            if storage.load_class(arg[0]) is None:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg and storage.load_class(arg) is None:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            lst = []
            for p in objs:
                lst.append(str(objs[p]))
            print(lst)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
