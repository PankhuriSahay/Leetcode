# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        ans = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)

        return ans[k - 1]