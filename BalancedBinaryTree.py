'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
'''


class Solution:

    def is_leaf(self, root: TreeNode) -> bool:
        return not root.left and not root.right

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if self.is_leaf(root):
            root.height = 1
            return True
        elif not root.left and root.right:
            if self.is_leaf(root.right):
                root.height = 2
                return True
            return False
        elif root.left and not root.right:
            if self.is_leaf(root.left):
                root.height = 2
                return True
            return False
        elif self.isBalanced(root.left) and self.isBalanced(root.right):
            if abs(root.left.height - root.right.height) <= 1:
                root.height = max(root.left.height, root.right.height) + 1
                return True
            return False
        return False
