"""

ven a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

Input:
    2
   / \
  1   3
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

"""

class Solution:

    """
        cost: 180ms >5.03
        https://leetcode.com/submissions/detail/212553748/
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not self.compare(root.left, root.val, True) or not self.compare(root.right, root.val, False):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)


    def compare(self, root: TreeNode, base: int, left: bool) -> bool:
        if not root:
            return True

        if left and base <= root.val:
            print('%s,%s,%s' % (left, base, root.val))
            return False

        if not left and base >= root.val:
            print('%s,%s,%s' % (left, base, root.val))
            return False

        return self.compare(root.left, base, left) and self.compare(root.right, base, left)
