# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        dfs(root)

        return self.diameter