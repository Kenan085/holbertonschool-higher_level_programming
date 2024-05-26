#!/usr/bin/python3
'''
Documentation for module that defines singly linked list
'''

class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the linked list."""
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]  # Remove trailing newline

    def sorted_insert(self, value):
        """Inserts a new node into the sorted linked list."""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None and value >= current.next_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
