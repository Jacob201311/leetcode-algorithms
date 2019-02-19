"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

     3
    / \
   5   1
  / \   \ \
 6   2  9  8
    / \
   7   4


For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.

"""

class Solution:

    """
        cost: 36ms >98.52
        memory: 12.5MB <100
        https://leetcode.com/submissions/detail/208987839/
    """
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        result1 = []
        result2 = []
        self.leafSequence(root1, result1)
        self.leafSequence(root2, result2)

        return result1 == result2

    def leafSequence(self, root: 'TreeNode', result: 'List[int]') -> 'void':
        if not root:
            return

        if not root.left and not root.right:
            result.append(root.val)

        self.leafSequence(root.left, result)
        self.leafSequence(root.right, result)

