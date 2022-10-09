#!/usr/bin/python3

"""An interactive shell?"""

import cmd
import re
import sys
import models
from models.base_model import BaseModel
from models.__init__ import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)  ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
               }

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_EOF(self, line):
        """Exits console"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("Good Bye!")
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ overwriting the emptyline method """
        return False
        # OR
        # pass

    def do_create(self, args):
        """ Create an object of any class"""
        pattern = """(^\w+)((?:\s+\w+=[^\s]+)+)?"""
        m = re.match(pattern, args)
        args = [s for s in m.groups() if s] if m else []

        if not args:
            print("** class name missing **")
            return

        className = args[0]

        if className not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        kwargs = dict()
        if len(args) > 1:
            params = args[1].split(" ")
            params = [param for param in params if param]
            for param in params:
                [name, value] = param.split("=")
                if value[0] == '"' and value[-1] == '"':
                    value = value[1:-1].replace('_', ' ')
                elif '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                kwargs[name] = value

        new_instance = HBNBCommand.classes[className]()

        for attrName, attrValue in kwargs.items():
            setattr(new_instance, attrName, attrValue)

        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, line):
        """print <class name> <id>"""
        arr = line.split()    # split & assign to varia

        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_str])

    def do_destroy(self, line):
        """Destroy command deletes an instance based on the class name and id
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_str)
            #    del (storage.all()[new_str])
                storage.save()

    # def do_all(self, line):
    #    """ Print all instances in string representation """
    #    new_list = []

    #    if not line:
    #        for key, obj in storage.all().items():
    #            new_list.append(str(obj))
    #        print(new_list)
    #    elif line not in class_home:
    #        print("** class doesn't exist **")
    #    else:
    #        for key, obj in storage.all().items():
    #            if obj.__class__.__name__ == line:
    #                new_list.append(str(obj))
    #        print(new_list)

    def do_all(self, line):
        """ Print all instances in string representation """
        objects = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            st = line.split(" ")
            if st[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == st[0]:
                        objects.append(str(value))
                print(objects)

    # def do_all(self, line):
    #    """ Print all instances in string representation """
    #    arr = line.split()
    #    if len(arr) > 0 and arr[0] not in storage.class_dict():
    #        print("** class doesn't exist **")
    #    else:
    #        new_list = []
    #        for obj in storage.all().values():
    #            if len(arr) > 0 and arr[0] == obj.__class__.__name__:
    #                new_list.append(obj.__str__())
    #            elif len(arr) == 0:
    #                new_list.append(obj.__str__())
    #        print(new_list)

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        usage:  update <class> <id> <attribute_name> <attribute_value> or
                <class>.update(<id>, <attribute_name>, <attribute_value>) or
                <class>.update(<id>, <dictionary>)
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], arr[2], arr[3])
                storage.save()

    def do_count(self, line):
        """Print the count all class instances"""
        kclass = globals().get(line, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
        print(count)

    def default(self, line):
        if line is None:
            return

        cmdPattern = "^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        paramsPattern = """^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        m = re.match(cmdPattern, line)
        if not m:
            super().default(line)
            return
        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
