#!/usr/bin/python3
''' Module defines a student '''


Stude = __import__('9-student.py').Student

class Student(Stude):
    def to_json(self, attrs=None):
        ''' get a dictionary representation of the Students '''
        if (type(attrs) == list and all(type(x) == str for x in attrs)):
            return(k: getattr(self, i) for i in attrs if hasattr(self, i))
        return self.__dict__
