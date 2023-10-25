# no.515
from typing import Optional, List
from utils import TreeNode, insert_tree_node

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cache = [root]
        ans = [root.val]
        while len(cache):
            vals, new_cache = [], []
            for node in cache:
                if node.left:
                    if node.left.val is not None:
                        vals.append(node.left.val)
                    new_cache.append(node.left)
                if node.right:
                    if node.right.val is not None:
                        vals.append(node.right.val)
                    new_cache.append(node.right)
            if len(vals):
                ans.append(max(vals))
            cache = new_cache
        return ans


def create_tree(vals):
    root = TreeNode(vals[0])
    for i in vals[1:]:
        insert_tree_node(i, root)
    return root


if __name__ == '__main__':
    root = create_tree([1, 3, 2, 5, 3, None, 9])
    sol = Solution()
    print(sol.largestValues(root))
    root = create_tree([1, 2 ,3])
    print(sol.largestValues(root))
   


