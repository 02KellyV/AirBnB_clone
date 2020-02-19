#!/usr/bin/python3
import cmd
import models

"""
"""
classes_dict = {
    'BaseModel': BaseModel,
}


class HBNBCommand(cmd.Cmd):
    collection_keys = classes_dict.keys()
    prompt = '(hbnb)'

    def do_quit(self, _input):
        return True

    def do_EOF(self, _input):
        return True

    def emptyline(self):
        return False

    def do_create(self, _input_class_name):
        """Creates a new instance of BaseModel in JSON"""
        if not _input_class_name:
            print("** class name missing **")
            return
        if _input_class_name not in BaseModel:
            print("** class doesn't exist **")
            return
        newinstance = classes_dict[_input_class_name]()
        newinstance.save()
        print(newinstance.id)

    def do_show(self, _input):
        input2 = _input
        if len(input2.split(' ')[0]) is 0:
            print("** class name missing **")
            return
        if input2.split(' ')[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return
        if len(input2.split) is 1:
            print("** instance id missing **")
            return

        models.storage.reload()
        for key, value in models.storage.all().items():
            if value.__class__.__name__ == input2[0] and value.id == input2[1]:
                print(value.__str__())
                return
        print("** no instance found **")

    def do_destroy(self, _input):
        if len(_input.split(' ')[0]) is 0:
            print("** class name missing **")
            return
        if _input.split(' ')[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return
        if len(_input.split) is 1:
            print("** instance id missing **")
            return

        models.storage.reload()
        delint = models.storage.all()
        for key, value in delint.items():
            if value.__class__.__name__ == _input[0] and value.id == _input[1]:
                del(delint[key])
                return
        print("** no instance found **")

    def all(self, _input_class):
        if _input_class:
            if _input_class not in self.collection_keys:
                print("** class doesn't exist **")
        for key_items in models.storage.all().keys():
            key_items = models.storage.all()[key_items]
            print(key_items)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
