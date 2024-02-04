#no. 1043

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = []
        for i in range(n):
            dp.append(0)
        dp[n - 1] = arr[n - 1]
        dp.append(0)
        for start in range(n - 2, -1, -1):
            curr_max = 0
            end = min(start + k, n)
            for i in range(start, end):
                curr_max = max(arr[i], curr_max)
                dp[start] = max(dp[start], dp[i + 1] + curr_max * (i - start + 1))
        return dp[0]
