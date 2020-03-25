"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""

class Solution:
    def __init__(self):
        self.resultDict = {}

    """
	cost: 24 ms > 84.04
	memory: > 98.51
	https://leetcode.com/submissions/detail/315693672/
	tc: O(n)
	sc: O(n)
    """
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        if self.resultDict.get(n):
            return self.resultDict[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = self.climbStairs(n - 1) + self.climbStairs(n-2)
        self.resultDict[n] = result
        return result

    """
	use dp
    """
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        if n == 1:
            return 1;

        f1 = 1
        f2 = 2
        for i in range(3, n + 1):
            f1, f2= f2, f1 + f2

        return f2
