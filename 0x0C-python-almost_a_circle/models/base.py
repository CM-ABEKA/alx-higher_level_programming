'''
Base class for models
'''


class Base():
    __nb_objects = 0

    def __init__(self, id):
        if id:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
