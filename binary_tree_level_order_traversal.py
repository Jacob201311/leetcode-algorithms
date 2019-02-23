"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""

class Solution:

    """
        cost: 44ms >51.86
        https://leetcode.com/submissions/detail/209992669/
    """
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        result = []
        self.collect(root, result, 0)
        return result

    def collect(self, root: 'TreeNode', result: 'List[List[int]]', level: 'int'):
        if not root:
            return

        if len(result) -1 < level:
            result.append([])

        result[level].append(root.val)
        nextLevel = level + 1
        self.collect(root.left, result, nextLevel)
        self.collect(root.right, result, nextLevel)
