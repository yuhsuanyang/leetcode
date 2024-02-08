# no. 279
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        squares = []
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n):
            if i ** 2 > n:
                break
            else:
                squares.append(i ** 2)
                dp[i ** 2] = 1 

        for i in range(1, n+1):
            if not dp[i]:
                min_ = dp[i - 1]
                for num in squares:
                    if num > i:
                        break
                    min_ = min(min_, dp[i - num])
                dp[i] = min_ + 1
        return dp[-1]


