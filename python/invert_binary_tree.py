# no. 226
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
        def invertTree(self, root:TreeNode) -> TreeNode:
            if root == None:
                return None
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            return root
