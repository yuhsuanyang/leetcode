# no.102
from utils import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            row = []
            next_row = []
            for node in queue:
                row.append(node.val)
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            ans.append(row)
            queue = next_row
        return ans
