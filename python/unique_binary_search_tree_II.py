# no.95
from typing import List, Optional
from utils import TreeNode

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def get_trees(start, end):
            if start > end:
                return [None]
            elif start == end:
                return [TreeNode(start)]
            result = []
            for root in range(start, end + 1):
                lefts = get_trees(start, root - 1)
                rights = get_trees(root + 1, end)
                for left_tree in lefts:
                    for right_tree in rights:
                        result.append(TreeNode(root, left_tree, right_tree))
            return result
        return get_trees(1, n)
   
if __name__ == '__main__':
    sol = Solution()
    for i in range(1, 9):
        ans = sol.generateTrees(i)
#        print(ans)
        print(len(ans))
        print('-' * 20)
