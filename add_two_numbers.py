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
    def addTwoNumbers_v1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_length = 1
        l2_length = 1
        l1_new = l1
        l2_new = l2
        while l1_new.next or l2_new.next:
            if l1_new.next:
                l1_length += 1
                l1_new = l1_new.next
            if l2_new.next:
                l2_length += 1
                l2_new = l2_new.next

        if l1_length - l2_length >= 0:
            while l1_length - l2_length - 1 >= 0:
                l2_length += 1
                l = ListNode(0)
                l.next = l2
                l2 = l
        else:
            while l2_length - l1_length - 1 >= 0:
                l1_length += 1
                l = ListNode(0)
                l.next = l1_new
                l1 = l

        l3 = ListNode(0)
        l4 = l3
        l3.next = l4
        carry = 0
        while l1:
            l3_temp = ListNode(l1.val + l2.val + carry)
            if l3_temp.val - 9 > 0:
                carry = 1
                l3_temp.val = l3_temp.val - 10
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next
            l4.next = l3_temp
            l4 = l3_temp

        if carry == 1:
            l4.val = l4.val - 10
            l4.next = ListNode(1)

        return l3.next

if "__main__" == __name__:
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    l3 = solution.addTwoNumbers_v1(l1, l2)
    while l3:
        print(l3.val, " -> ")
        l3 = l3.next


