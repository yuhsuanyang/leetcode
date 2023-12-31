# no. 1624
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for i in range(len(s)):
            c = s[i]
            for j in range(len(s) - 1, 0, -1):
                if s[j] == c:
                    length_between_equal = j - i - 1
                    if length_between_equal > ans:
                        ans = length_between_equal
                    break
        return ans

        
