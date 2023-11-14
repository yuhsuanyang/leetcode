#no.1930
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = {}
        for i, j in enumerate(s):
            if j not in counter:
                counter[j] = [i]
            else:
                counter[j].append(i)
        pan = set()
        ans = 0
        for key in counter:
            if len(counter[key]) > 1:
                start = counter[key][0] + 1
                end = counter[key][-1]
                for j in range(start, end):
                    pan.add(s[j])
            ans += len(pan)
            pan.clear()
        return ans
