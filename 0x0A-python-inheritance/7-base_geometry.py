#!/usr/bin/python3
''' Module - Integer Validator '''


class BaseGeometry:
    ''' SuperClass to implement geomerical shapes '''

    def area(self):
        ''' raise exception when called '''
        raise Esception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' checks an integer value
            Args:
            @name: string of name of the value
            @value: integer value

            Raises:
                TypeError: If value is not integer
                ValueError: if value is less than or equal to 0
        '''
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
