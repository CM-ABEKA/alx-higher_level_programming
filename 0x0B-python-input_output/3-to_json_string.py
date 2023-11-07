#!/usr/bin/python3
''' Module Json representation of string '''
import json


def to_json_string(my_obj):
    ''' returns a JSON representation of a string '''

    j_data = json.dumps(my_obj)
    return j_data
