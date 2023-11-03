# no. 1441
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        actions = []
        i, j = 1, 0
        while (i <= n and j < len(target)):
            actions.append('Push')
            if target[j] != i: 
                actions.append('Pop')
            else:
                j += 1
            i += 1
        return actions
                    
