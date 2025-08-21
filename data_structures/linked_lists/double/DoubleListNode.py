from data_structures.linked_lists.ListNode import ListNode

class DoubleListNode(ListNode):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None
        self.next = None