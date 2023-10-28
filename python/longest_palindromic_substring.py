# no.5

class Solution:
    def checkPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return
            start += 1
            end -= 1
        return s

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or self.checkPalindrome(s):
            return s
        longest = s[0]
        for i in range(len(s)):
            if i + len(longest) >= len(s):
                continue
            for j in range(i + len(longest), len(s) + 1):
                candidate = self.checkPalindrome(s[i: j])
                if candidate and len(candidate) > len(longest):
                    longest = candidate
        return longest 


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('222020221'))
    print(sol.longestPalindrome('cbbd'))


