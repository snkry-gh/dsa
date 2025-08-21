"""
Implementation of Single Linked Lists
"""

from data_structures.linked_lists.LinkedList import LinkedList
from data_structures.linked_lists.single.SingleListNode import SingleListNode


class SingleList(LinkedList):

    def __init__(self):
        super().__init__()
    
    def push_front(self, data):
        node = SingleListNode(data)
        node.next = self._head
        self._head = node
        if self._tail is None: self._tail = node
        self._size += 1

    def push_back(self, data):
        node = SingleListNode(data)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop_front(self):
        if super().__underflow(): raise IndexError("Linked List Empty")
        
        node = self._head
        self._head = node.next
        if self._head is None: self._tail = None
        self._size -= 1
        return node.data
    
    def pop_back(self):
        if super().__underflow(): raise IndexError("Linked List Empty")
        
        if self._head is self._tail:
            node = self._head.data
            self._head = self._tail = None
            self._size -= 1
            return node
        
        prev = self._head
        while prev.next is not self._tail:
            prev = prev.next
        node = self._tail.data
        prev.next = None
        self._tail = prev
        self._size -= 1
        return node
