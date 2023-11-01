# no.501

from utils import TreeNode
from typing import Optional

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
           return [root.val]
        cache = [root]
        counter = {root.val: 1}
        max_ = 1
        while len(cache):
            temp = cache[0]
            cache = cache[1:]
            if temp.left:
                cache.append(temp.left)
                if temp.left.val not in counter:
                    counter[temp.left.val] = 1
                else:
                    counter[temp.left.val] += 1
                if counter[temp.left.val] > max_:
                    max_ = counter[temp.left.val]
            if temp.right:
                cache.append(temp.right)
                if temp.right.val not in counter:
                    counter[temp.right.val] = 1
                else:
                    counter[temp.right.val] += 1
                if counter[temp.right.val] > max_:
                    max_ = counter[temp.right.val]
        ans = [i for i in counter if counter[i] == max_]
        return ans
