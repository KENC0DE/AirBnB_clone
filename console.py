#!/usr/bin/python3
"""
### Command Interpreter ###
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter Class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit """
        exit()

    def do_EOF(self, arg):
        """ quit """
        print()
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
