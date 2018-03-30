"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:

    """
	52ms
	>71.78
	https://leetcode.com/submissions/detail/147674150/
    """
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
            for num2 in nums[i + 1:]:
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

    """
	3580ms
	>23.36
	https://leetcode.com/submissions/detail/147673640/
    """
    def twoSum_v2(self, nums, target):
        for i, num in enumerate(nums):
            left_value = target - num
            for j, num2 in enumerate(nums[i + 1:]):
                if num2 == left_value:
                    return [i, j + i + 1]


    """
	48ms
	>74.71
	https://leetcode.com/submissions/detail/147681286/
    """
    def twoSum_v3(self, nums, target):
          def _filter_num(x):
              if reverse:
                  return x >= target
              else:
                  return x < target

          num_dict = {}
          for i, num in enumerate(nums):
              if num_dict.get(num):
                  num_dict[num].append(i)
              else:
                  num_dict[num] = [i]

          reverse = 0 >= target
          nums = list(filter(_filter_num, nums))
          nums.sort(reverse=reverse)

          for num in nums:
              left_value = target - num
              if num_dict.get(left_value):
                  if left_value == num:
                      return num_dict[num][:2]
                  else:
                      num_dict[num].extend(num_dict[left_value])
                      return num_dict[num]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum_v3([3,3], 6))
