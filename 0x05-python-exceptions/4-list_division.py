#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide two lists element by element and handle various exceptions.
    
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
        
    Returns:
        list: A new list of length list_length containing the divisions.
        In case of exceptions (TypeError, ZeroDivisionError, or IndexError),
        corresponding error messages are printed, and 0 is placed in the result list.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            div = 0
        except ZeroDivisionError:
            print("Division by 0")
            div = 0
        except IndexError:
            print("Out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
