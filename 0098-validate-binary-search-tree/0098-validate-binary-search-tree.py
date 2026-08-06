# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
       def dfs(node, minimum, maximum):
           if node is None:
               return True
           if node.val <= minimum or node.val >= maximum:
               return False

           return (dfs(node.left, minimum, node.val) and
                  dfs(node.right, node.val, maximum))

       return dfs(root, float("-inf"), float("inf"))