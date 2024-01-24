# no. 94
from utils import TreeNode

# left, middle, right
class Solution:
    def __init__(self):
        self.result = []
    
    def helper(self, root: Optional[TreeNode]):
        if not root:
            return
        if root.left:
            self.helper(root.left)
        self.result.append(root.val)
        if root.right:
            self.helper(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        return self.result
