"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
"""

class Solution:

    def __init__(self):
        self.max = 0

    """
        cost: 800ms >8.28
        https://leetcode.com/submissions/detail/213046084/
    """
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return self.max

        tmp1 = self.pathSum(root.left, root.val, 0)
        tmp2 = self.pathSum(root.right, root.val, 0)

        if self.max < (tmp1 + tmp2):
            self.max = (tmp1 + tmp2)

        self.longestUnivaluePath(root.left)
        self.longestUnivaluePath(root.right)
        return self.max

    def pathSum(self, root:TreeNode, baseVal: int, length: int) -> int:
        if not root:
            return length

        if root.val == baseVal:
            length += 1
        else:
            return length

        return max(self.pathSum(root.left, root.val, length), self.pathSum(root.right, root.val, length))
