'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        answer = []

        def dfs(node, s):
            if node is None:
                return
            if node.left is None and node.right is None and s == node.val:
                answer.append(1)
                return
            if answer:
                return
            dfs(node.left, s - node.val)
            dfs(node.right, s - node.val)
        dfs(root, sum)
        return answer