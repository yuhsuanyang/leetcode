#no. 1609
from utils import TreeNode

class Solution:
    def validate_even_row(self, vec: List[int]):
        if vec[-1] % 2 == 0:
            return False
        for i in range(len(vec) - 1):
            if(vec[i] >= vec[i+1]) or (vec[i] % 2 == 0):
                return False
        return True

    def validate_odd_row(self, vec: List[int]):
        if vec[-1] % 2 == 1:
            return False
        for i in range(len(vec) - 1):
            if(vec[i] <= vec[i+1]) or (vec[i] % 2 == 1):
                return False
        return True

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        counter = 0
        while queue:
            row = []
            next_row = []
            for node in queue:
                row.append(node.val)
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            if counter % 2: # odd
                ans = self.validate_odd_row(row)
            else: # even
                ans = self.validate_even_row(row)
            if not ans:
                return False
            queue = next_row
            counter += 1
        return True
