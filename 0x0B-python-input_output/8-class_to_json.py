#1/usr/bin/python3
''' Module dict description for JSON serialization '''


def class_to_json(obj):
    ''' returns dictionary description with simple data
        structure for a JSON serialization of objects
    '''
    return obj.__dict__
