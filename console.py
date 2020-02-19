#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
"""
"""
classes_dict = {
    'BaseModel': BaseModel,
}


class HBNBCommand(cmd.Cmd):
    classes_dict.keys()
    prompt = '(hbnb)'

    def do_quit(self, _input):
        return True

    def do_EOF(self, _input):
        return True

    def emptyline(self):
        return False

    def do_create(self, _input_class_name):
        if not _input_class_name:
            print("** class name missing **")
            return
        if _input_class_name not in BaseModel
            print("** class doesn't exist **")
            return
        newinstance = classes_dict[_input_class_name]()
        newinstance.save()
        print(newinstance.id)

    def do_show(self):
        if len(_input.split(' ')[0]) is 0:
            print("** class name missing **")
            return
        if _input.split(' ')[0] not in classes_dict:
            print("** class doesn't exist **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
