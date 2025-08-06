"""
Implementation of Double Linked Lists
"""

from data_structures.linked_lists.LinkedList import LinkedList
from data_structures.linked_lists.double.DoubleListNode import DoubleListNode

class DoubleLinkedList(LinkedList):
    
    def __init__(self):
        super().__init__()
    
    def push_front(self, data):
        node = DoubleListNode(data)
        node.next = self._head
        if self._head: self._head.prev = node
        self._head = node
        if self._tail is None: self._tail = node
        self._size += 1

    def push_back(self, data):
        node = DoubleListNode(data)
        node.prev = self._tail
        if self._tail: self._tail.next = node
        self._tail = node
        if self._head is None: self._head = node
        self._size += 1

    def pop_front(self):
        if super().__underflow(): raise IndexError("Linked List Empty")
        node = self._head
        self._head = node.next
        if self._head: self._head.prev = None
        else: self._tail = None
        self._size -= 1
        return node.data
    
    def pop_back(self):
        if super().__underflow(): raise IndexError("Linked List Empty")
        node = self._tail
        self._tail = node.prev
        if self._tail: self._tail.next = None
        else: self._head = None
        self._size -= 1
        return node.data
