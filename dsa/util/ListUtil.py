from data_structures.linked_lists.single.SingleList import SingleList
from data_structures.linked_lists.double.DoubleList import DoubleList

def createSingleList(arr):
    lst = SingleList()
    for x in arr:
        lst.push_back(x)
    return lst._head

def createDoubleList(arr):
    lst = DoubleList()
    for x in arr:
        lst.push_back(x)
    return lst._head

def createCyclicList(head, start):
    if head is None or start < 0:
        return head

    target = head
    idx = 0
    while target is not None and idx < start:
        target = target.next
        idx += 1
    if target is None:
        return head

    tail = head
    while tail.next is not None:
        tail = tail.next

    tail.next = target
    return head

def printList(head):
    elements = []
    curr = head
    while curr is not None:
        elements.append(str(curr.data))
        curr = curr.next
    output = " -> ".join(elements)
    print(output)
