# no. 98
from utils import TreeNode
from typing import Optional

class Solution:
    def __init__(self):
        self.ans = True
    def get_extreme(self, root, mode):
        left = root.val
        right = root.val
        if root.left:
            left = self.get_extreme(root.left, mode)
            if mode == 'max' and left >= root.val:
                self.ans = False
        if root.right:
            right = self.get_extreme(root.right, mode)
            if mode == 'min' and right <= root.val:
                self.ans = False
        if mode == 'max':
            return max(left, right)
        elif mode == 'min':
            return min(left, right)
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.get_extreme(root, 'max')
        if self.ans:
            self.get_extreme(root, 'min')
        return self.ans

