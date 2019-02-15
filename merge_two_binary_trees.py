"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""
class TreeNode:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and not t2:
            return t1
        elif not t1 and t2:
            return t2
        elif not t1 and not t2:
            return None
        else:
            t1.value += t2.valu
            mergeTrees(t1.left_node, t2.left_node)
            mergeTrees(t1.right_node, t2.right_node)



