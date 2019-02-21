"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet (https://twitter.com/mxcl/status/608682016205344768) by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

class Solution:

    """
        cost: 32ms >100
        memory: 12.3MB <94.67
        https://leetcode.com/submissions/detail/209497518/
    """
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        return self.buildTree(root, TreeNode(0))

    def buildTree(self, origin: 'TreeNode', fresh: 'TreeNode'):
        if not origin:
            return fresh

        fresh.val = origin.val

        if origin.left:
            fresh.right = TreeNode(0)

        if origin.right:
            fresh.left = TreeNode(0)

        self.buildTree(origin.left, fresh.right)
        self.buildTree(origin.right, fresh.left)

        return fresh
