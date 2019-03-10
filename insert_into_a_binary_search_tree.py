"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""

class Solution:

    """
        cost: 136ms >34.77
        https://leetcode.com/submissions/detail/213754770/
    """
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        self.origin = root
        self.last = None
        self.change = False

        def helper(root: TreeNode):
            if not root:
                return

            helper(root.left)
            self.last = root

            if self.change:
                return

            if root.val > val:
                tmp = TreeNode(val)
                tmp.left = root.left
                root.left = tmp
                self.change = True
                return
            helper(root.right)

        helper(root)
        if not self.change and self.last:
            self.last.right = TreeNode(val)
        return self.origin
