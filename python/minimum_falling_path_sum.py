# no. 931
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[] for i in range(n - 1)]
        dp.append(matrix[-1])
        for row in range(n - 2, -1, -1):
            for col in range(n):
                if col == 0:
                    min_ = min(dp[row + 1][col], dp[row + 1][col + 1])
                elif col == n - 1:
                    min_ = min(dp[row + 1][col], dp[row + 1][col - 1])
                else:
                    min_ = min(dp[row + 1][col], dp[row + 1][col - 1], dp[row + 1][col + 1])
                dp[row].append(matrix[row][col] + min_)
        return min(dp[0])
