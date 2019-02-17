"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    """
        cost: 40ms >99.75
        memory:12.6MB <100
        https://leetcode.com/submissions/detail/208436355/
    """
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False

        return self.checkSymmetic(root.left, root.right)



    def checkSymmetic(self, left: 'TreeNode', right: 'TreeNode') -> 'bool':
        if not left and not right :
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.checkSymmetic(left.left, right.right) \
            and self.checkSymmetic(left.right, right.left)
