"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

class Solution:

    """
        cost: 60ms >60.01
        https://leetcode.com/submissions/detail/210561286/
    """
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []

        answer = []
        resultList = self.collect(root)
        for result in resultList:
            if sum(result) == s:
                result.reverse()
                answer.append(result)
        return answer


    def collect(self, root: TreeNode):
        if not root:
            return []

        if not root.left and not root.right:
            return [[root.val]]

        leftResult = self.collect(root.left)

        if leftResult:
            for inLeftResult in leftResult:
                inLeftResult.append(root.val)


        rightResult = self.collect(root.right)
        if rightResult:
            for inRightResult in rightResult:
                inRightResult.append(root.val)

        return leftResult + rightResult
