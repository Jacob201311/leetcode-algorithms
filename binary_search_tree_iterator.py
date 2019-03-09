"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:

      7
     / \
    3   15
        / \
       9  20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false



Note:

    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

"""
    cost: 92ms >77
    https://leetcode.com/submissions/detail/213462106/
"""
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = []

        def inOrder(root: TreeNode):
            if not root:
                return
            inOrder(root.left)
            self.queue.append(root.val)
            inOrder(root.right)

        inOrder(root)
        self.queue = deque(self.queue)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.queue.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.queue) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
