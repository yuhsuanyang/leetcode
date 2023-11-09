# no. 1759
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 1
        curr_streak = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                curr_streak += 1
            else:
                curr_streak = 1
            ans += curr_streak
        return ans % (10**9 + 7)
