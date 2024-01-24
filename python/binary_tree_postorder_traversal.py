# no. 145
from utils import TreeNode

# middle, left, right
class Solution:
    def __init__(self):
        self.result = []
    
    def helper(self, root: Optional[TreeNode]):
        if not root:
            return
        self.result.append(root.val)
        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        return self.result
