#!/usr/bin/python3
"""
### Command Interpreter ###
"""


import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter Class """

    prompt = "(hbnb) "

    def default(self, arg):
        """ Default command """
        custom_cmd = ["all()", "count()"]
        segs = arg.split('.')
        if segs[0] in storage.load_class() and segs[1] in custom_cmd:
            cLs = storage.load_class(segs[0])
            uls = []
            fobj = self.filter(cLs)
            for p in fobj:
                uls.append(str(p))
            if segs[1] == custom_cmd[0]:
                print(uls)
            elif segs[1] == custom_cmd[1]:
                print(len(uls))
        elif segs[0] in storage.load_class():
            dlm = re.split(r'[.()",]', arg)
            dlm = [i for i in dlm if i != '']
            if dlm[1] and hasattr(self, 'do_' + dlm[1]):
                tmp = (dlm[1])[:]
                del dlm[1]
                dlm = " ".join(dlm)
                line = str(tmp) + " " + dlm
                self.onecmd(line)

    def filter(self, name):
        """ filter objects """
        obj_dict = storage.all()
        obj_ls = list(obj_dict.values())
        filt = [obj for obj in obj_ls if type(obj) is name]
        return filt

    def do_quit(self, arg):
        """ Quit Program """
        return True

    def do_EOF(self, arg):
        """ Quit Program """
        return True

    def emptyline(self):
        """an empty line"""
        pass

    def do_create(self, arg):
        """ Create Object """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif storage.load_class(arg) is None:
            print("** class doesn't exist **")
        else:
            new_obj = storage.load_class(arg)()
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

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            pattern = r'["\']([^"\']*?)["\']'
            tokens = re.split(r'\s+|' + pattern, arg)
            arg = [token for token in tokens if token]
            if storage.load_class(arg[0]) is None:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif len(arg) < 3:
                    print("** attribute name missing **")
                elif len(arg) < 4:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    attar = storage.attrib(arg[2])
                    if attar:
                        arg[3] = attar(arg[3])
                    setattr(obj, arg[2], arg[3])
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
