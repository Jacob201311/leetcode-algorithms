"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:
    1
   / \
  2   3
 /
4
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
    1
   / \
  2   3
   \   \
    4   5

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
    1
   / \
  2   3
   \
    4

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.

"""

class Solution:
    def __init__(self):
        self.d = []
        self.p = []

    """
        cost:40ms >27.69
        https://leetcode.com/submissions/detail/211066622/
    """
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        self.getParent(root, x, y, 0)

        if self.d[0] - self.d[1] == 0 and self.p[0] - self.p[1] != 0:
            return True
        return False

    def getParent(self, root: TreeNode, x: int, y: int, depth: int):
        if not root:
            return

        depth += 1
        if root.left and (root.left.val == x or root.left.val == y):
            print('left:%d,%d' % (depth, root.val))
            self.d.append(depth)
            self.p.append(root.val)

        if root.right and (root.right.val == x or root.right.val == y):
            print('right:%d,%d' % (depth, root.val))
            self.d.append(depth)
            self.p.append(root.val)

        self.getParent(root.left, x, y, depth)
        self.getParent(root.right, x, y, depth)

