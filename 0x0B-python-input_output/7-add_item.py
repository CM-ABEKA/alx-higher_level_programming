#!/usr/bin/python3
''' Module add argumenst to Python list '''
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        result = load_from_js('add_item.json')
    except FileNotFoundError:
        result = []
    result.extend(sys.argv[1:])
    save_to_json_file(result, 'add_item.json')
