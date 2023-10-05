# no.700
from utils import TreeNode

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root
        if not root.left and not root.right:
            return
        left_ans = self.searchBST(root.left, val)
        right_ans = self.searchBST(root.right, val)
        if left_ans:
            return left_ans
        if right_ans:
            return right_ans
        return
