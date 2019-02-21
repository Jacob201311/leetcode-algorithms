"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:

    """
       cost: 52ms >85.92
       memory: 12.5MB <70.84
       https://leetcode.com/submissions/detail/209563314/
    """
    def reverse(self, x: 'int') -> 'int':
        stack = [c for c in str(x if x > 0 else -1 * x)]
        a = ''
        while stack:
            a += stack.pop()

        b = int(a) if x > 0 else -1 * int(a)
        return b if b <= 2**31 -1 and b >= -2**31 else 0
