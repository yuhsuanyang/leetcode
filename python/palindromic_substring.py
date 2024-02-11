# no. 647

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        n = len(s)
        for i in range(n):
            row = [0 for _ in range(n)]
            dp.append(row)
        ans = 0
        for diff in range(0, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j]:
                    if diff <= 1:
                        dp[i][j] = 1
                        ans += 1
                    else:
                        if dp[i + 1][j - 1]:
                            dp[i][j] = 1
                            ans += 1
        return ans             
