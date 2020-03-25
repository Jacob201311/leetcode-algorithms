"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3
    Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""

ass NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = {}

    """
	cost: 6604ms >9.26
        memory: > 10.00
	https://leetcode.com/submissions/detail/315773872/
	tc: O(n) before no cache
        sc: O((1+n)n/2) = O(n^2)
    """
    def sumRange(self, i: int, j: int) -> int:
        cacheKey = str(i) + '_' + str(j)
        if self.cache.get(cacheKey):
            return self.cache[cacheKey]

        result = 0
        for x in range(i, j + 1):
            result += self.nums[x]
        self.cache[cacheKey] = result
        return result
