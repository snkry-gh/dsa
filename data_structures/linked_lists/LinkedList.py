from abc import ABC, abstractmethod

class LinkedList(ABC):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def index_of(self, data):
        curr, idx = self._head, 0
        while curr:
            if curr.data == data:
                return idx
            curr, idx = curr.next, idx + 1
        return -1

    def _underflow(self):
        return self._size == 0

    def _length(self):
        return self._size

    @abstractmethod
    def push_front(self, data):
        raise NotImplementedError
    
    @abstractmethod
    def push_back(self, data):
        raise NotImplementedError
    
    @abstractmethod
    def pop_front(self):
        raise NotImplementedError
    
    @abstractmethod
    def pop_back(self):
        raise NotImplementedError
    
    @abstractmethod
    def insert_at(self, data, idx):
        raise NotImplementedError
    
    @abstractmethod
    def remove_at(self, data, idx):
        raise NotImplementedError
    
    def index_of(self, data):
        curr, idx = self._head, 0
        while curr:
            if curr.data == data: return idx
            curr, idx = curr.next, idx+1
        return -1
