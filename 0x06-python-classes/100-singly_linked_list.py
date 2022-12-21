#!/usr/bin/python3

"""Define Node class for a singly-linked list."""


class Node:
    """Initialize a new Node."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set value of data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set value of next node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""
    def __init__(self):
        """Initialize new singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node."""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """String representation."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
