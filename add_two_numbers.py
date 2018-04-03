# coding=utf-8

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    """
	128ms
	>64.36
	https://leetcode.com/submissions/detail/148243044/
    """
    def addTwoNumbers_v1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        carry = 0
        l3_pointer = l3
        l3.next = l3_pointer
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            temp = ListNode(l1_val + l2_val + carry)
            if temp.val > 9:
                carry = 1
                temp.val = temp.val - 10
            else:
                carry = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3_pointer.next  = temp
            l3_pointer = l3_pointer.next


        if carry == 1:
            l3_pointer.next = ListNode(1)

        return l3.next




if "__main__" == __name__:
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l3 = solution.addTwoNumbers_v1(l1, l2)
    while l3:
        print(l3.val, " -> ")
        l3 = l3.next


