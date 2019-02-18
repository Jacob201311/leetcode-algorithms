"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:
     1
    / \
   1   1
  / \   \
 1   1   1

Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
     2
    / \
   2   2
  / \
 5   2

Input: [2,2,2,5,2]
Output: false

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""

class Solution:

    def __init__(self):
        self.val = None

    """
        cost: 36ms >79.82
        memory: 12.5MB <100
        https://leetcode.com/submissions/detail/208709167/
    """
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        if not self.val:
            self.val = root.val
        elif root.val != self.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
