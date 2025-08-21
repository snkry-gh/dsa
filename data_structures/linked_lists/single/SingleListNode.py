from data_structures.linked_lists.ListNode import ListNode

class SingleListNode(ListNode):
    def __init__(self, data):
        super().__init__(data)
        self.next = None

