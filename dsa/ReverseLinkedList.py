"""
Leetcode #206 | Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""

from dsa.util.ListUtil import *

class Solution:
    def reverseLinkedList(self):
        pass

    def solve(self):
        head = createSingleList([1, 2, 3, 4, 5])
        reverseHead = self.reverseLinkedList(head)
        printList(reverseHead)


def main():
    solution = Solution()
    solution.solve()

if __name__ == "__main__":
    main()
