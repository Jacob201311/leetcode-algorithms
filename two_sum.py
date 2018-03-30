"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[i] = num

        nums.sort()

        first_part_num = None
        second_part_num = None
        for i, num in enumerate(nums):
            left_value = target - num
            for num2 in nums[i:]:
                if num2 == left_value:
                    second_part_num = num2
                    first_part_num = num
                    break
            if second_part_num:
                break

        result = []
        for k, v in num_dict.items():
            if v == first_part_num:
                result.append(k)
                num_dict.pop(k)
                break

        for k, v in num_dict.items():
            if v == second_part_num:
                result.append(k)
                break

        return result

if __name__ == 'main':
	twoSum_v1([-1, -2, 0, 4], 4)
