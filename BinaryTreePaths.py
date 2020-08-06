'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []

        def getPaths(root, path):

            path += str(root.val)+"->"
            if root.left != None:
                p1 = getPaths(root.left, path)
                if root.right == None:
                    return p1
            if root.right != None:
                p2 = getPaths(root.right, path)
                if root.left == None:
                    return p2
            if root.left == None and root.right == None:
                return [path[:-2]]
            else:
                return p1 + p2
        paths = getPaths(root, "")
        return paths
