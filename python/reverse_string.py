from typing import List


class Solution:
    def reverseString(self, s: List[str], start=0, end=0):
        """
        Do not return anything, modify s in-place instead.
        """
        if end == 0:
            end = len(s) - 1
        if start >= end:
            return s
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        print(s)
        self.reverseString(s, start+1, end-1)


sol = Solution()
sol.reverseString(['h', 'e', 'l', 'l', 'o'], 0)
# sol.reverseString(['h', 'e', 'l'])

