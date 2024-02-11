# no.5

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = []
        n = len(s)
        for i in range(n):
            row = [0 for _ in range(n)]
            dp.append(row)
        ans = s[0]
        for diff in range(0, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j]:
                    if diff <= 1:
                        dp[i][j] = 1
                        ans = s[i: j + 1]
                    else:
                        if dp[i + 1][j - 1]:
                            dp[i][j] = 1
                            ans = s[i: j + 1]
        return ans            

