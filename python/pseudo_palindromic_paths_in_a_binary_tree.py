#no. 1457
from utils import TreeNode
class Solution:
    def __init__(self):
        self.value_count = [0 for _ in range(9)]
        self.result = 0

    def traverse(self, root):
        self.value_count[root.val - 1] += 1
        if not root.left and not root.right:
            #    print(self.value_count)
            num_odd = 0
            for i in self.value_count:
                if i % 2:
                    num_odd += 1
            if num_odd <= 1:
                self.result += 1
            self.value_count[root.val - 1] -= 1
            return
        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)
        self.value_count[root.val - 1] -= 1

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.result

