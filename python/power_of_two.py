#no. 231

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n <= 2:
            return True
        if n % 2:
            return False
        ans = self.isPowerOfTwo(n / 2)
        return ans
