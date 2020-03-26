"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution:

    def __init__(self):
        self.resultDict = {}

    """
	recursive + memoization, easy understand
    """
    def rob(self, nums: List[int]) -> int:
        # asssume the index is i
        # result = max(f(i-1), nums[i] + f(i-2))

        if not nums:
            return 0

        if self.resultDict.get(len(nums)):
            return self.resultDict[len(nums)]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        result = max(nums[-1] + self.rob(nums[:-2]), self.rob(nums[:-1]))
        self.resultDict[len(nums)] = result
        return result

    """
	cost: 32ms >37.08
	memory: > 97.73
	https://leetcode.com/submissions/detail/315988499/
	tc: O(n)
	sc: O(1)
    """
    def rob(self, nums: List[int]) -> int:
        # current = max(last + nums[i], current)

        current = last = 0
        for num in nums:
            result = max(current, num + last)
            last = current
            current = result

        return current

