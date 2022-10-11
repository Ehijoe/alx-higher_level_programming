#!/usr/bin/python3
"""Singly linked list."""


class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Create a node for a linked list."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data of the node."""
        return self.__data

    @data.setter
    def data(self, val):
        if type(val) is not int:
            raise TypeError("data must be an integer")
        self.__data = val

    @property
    def next_node(self):
        """Return the next node or None if there is no next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        if node is not None and type(node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = node


class SinglyLinkedList:
    """A sorted singly linked list."""

    def __init__(self):
        """Create an empty linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert an item into the linked list in sorted order."""
        if self.__head is None or self.__head.data > value:
            self.__head = Node(value, self.__head)
            return
        curr = self.__head
        while curr.next_node is not None and value > curr.next_node.data:
            curr = curr.next_node
        curr.next_node = Node(value, curr.next_node)

    def __repr__(self):
        """Return string representation of a linked list."""
        result = ""
        curr = self.__head
        while curr is not None:
            result += str(curr.data)
            if curr.next_node is not None:
                result += "\n"
            curr = curr.next_node
        return result
