#!/usr/bin/python3
''' Module writes Object to text file '''
import json


def save_to_json_file(my_obj, filename):
    ''' saves Object to a text file in JSON format '''
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
