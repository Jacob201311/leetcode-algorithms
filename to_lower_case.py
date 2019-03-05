"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

class Solution:

    """
        cost: 36ms >49.59
        https://leetcode.com/submissions/detail/212529953/
    """
    def toLowerCase(self, str: str) -> str:
        result = ''
        for el in str:
            if ord(el) >= ord('A') and ord(el) <= ord('Z'):
                result += chr(ord(el) - (ord('A') - ord('a')))
            else:
                result += el

        return result
