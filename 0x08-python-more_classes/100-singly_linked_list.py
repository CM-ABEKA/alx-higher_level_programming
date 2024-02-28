#!/usr/bin/python3
''' Singly Linked list object '''


class Node:
    ''' Node object '''
    def __init__(self, data, next_node=None):
        '''
        __init__(self, data): instantiate data field

        Fields:
        data: must be of type int
        next_node: pointer to next item
        Raises:
        TypeError: must be int
        TypeError(next_node): should be None or Node object
        self.data = data
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


''' SinglyLinkedList class '''


class SinglyLinkedList:
    ''' singly linked list object '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
