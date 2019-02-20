"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

    The range of node's value is in the range of 32-bit signed integer.

"""

class Solution:

    """
        cost: 56ms >96.17
        memory: 15.5MB <18.28
        https://leetcode.com/submissions/detail/209330783/
    """
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        result = []
        self.collect(root, result, 0)

        return [sum(levelResult) / len(levelResult) for levelResult in result]

    def collect(self, root, result, level):
        if not root:
            return
        else:
            if len(result) - 1 < level:
                result.append([])
            result[level].append(root.val)

        self.collect(root.left, result, level + 1)
        self.collect(root.right, result, level + 1)
