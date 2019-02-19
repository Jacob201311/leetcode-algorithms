"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""
class Solution:

    """
        cost: 44ms >99.96
        memory: 14.4MB <100
        https://leetcode.com/submissions/detail/209063711/
    """
    def maxDepth(self, root: 'TreeNode') -> 'int':
        return self.count(root, 0)

    def count(self, root: 'TreeNode', depth: 'int') -> 'int':
        if not root:
            return depth

        depth += 1
        return max(self.count(root.left, depth), self.count(root.right, depth))
