# no. 938
from utils import TreeNode
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        node_queue = [root]
        ans = 0
        while node_queue:
            curr_node = node_queue.pop(0)
            if curr_node:
                if curr_node.val > high:
                    node_queue.append(curr_node.left)
                elif curr_node.val < low:
                    node_queue.append(curr_node.right)
                else: # (curr_node.val >= low) and (curr_node.val <= high)
                    ans += curr_node.val
                    node_queue.append(curr_node.left)
                    node_queue.append(curr_node.right)
        return ans
