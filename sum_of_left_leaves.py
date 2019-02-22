"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

class Solution:

    """
        cost: 36ms >100
        memory: 13.5MB <5.32
        https://leetcode.com/submissions/detail/209800225/
    """
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        leveas = []
        self.collect(root, root, leveas)
        return int(sum(leveas) / 2)


    def collect(self, left: 'TreeNode', right: 'TreeNode',leftLeveas: 'List[int]'):
        if not left and not right:
            return

        if left:
            if not left.left and not left.right:
                print(left.val)
                leftLeveas.append(left.val)
            else:
                self.collect(left.left, left.right, leftLeveas)
        if right:
            self.collect(right.left, right.right, leftLeveas)
