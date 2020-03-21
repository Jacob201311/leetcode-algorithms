"""

ven a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def delete(parent, child, left, key):
            if not child:
                return
            if child.val == key:
                if not child.left and not child.right:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
                elif child.left and child.right:
                    pass
                else:
                    node = child.left if child.left else child.right
                    if left:
                        parent.left = node
                    else:
                        parent.right = node
                return

            delete(child, child.left, True, key)
            delete(child, child.right, False, key)
            return


        delete(root, root, True, key)
        return root
