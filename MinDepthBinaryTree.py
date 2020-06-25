'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.
'''


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            # empty node or empty tree
            return 0

        else:
            # DFS to find the shortest path from root to leaf node
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)

            if left and right:
                # Both left sub-tree and right sub-tree exist
                return min(left, right)+1

            elif left:
                # Only left sub-tree exists
                return left+1

            elif right:
                # Only right sub-tree exists
                return right+1

            else:
                # Leaf node
                return 1
