"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""

class Solution:

    """
        cost: 52ms >73.18
        https://leetcode.com/submissions/detail/210240214/
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.sum(root, 0, sum)

    def sum(self, root, pathSum: int, sum: int) -> bool:
        if not root:
            return False

        pathSum += root.val

        if not root.left and not root.right:
            if pathSum == sum:
                return True
            else:
                return False

        return self.sum(root.left, pathSum, sum) \
            or self.sum(root.right, pathSum, sum)
