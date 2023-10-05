# no. 1717
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        if len(s) == 1:
            return 0
        if x >= y:
            score1, leftover = self.search_pattern(s, 'ab', x)
            score2, _ = self.search_pattern(leftover, 'ba', y)
        else:
            score1, leftover = self.search_pattern(s, 'ba', y)
            score2, _ = self.search_pattern(leftover, 'ab', x)
        return score1 + score2

    def search_pattern(self, s, p, score):
        stack = ''
        if not s:
            return 0, stack
        result = 0
        for char in s:
            if not len(stack):
                stack += char
                continue
            if char == p[1] and stack[-1] == p[0]:
                stack = stack[:-1]
                result += score
            else:
                stack += char

        return result, stack


sol = Solution()
print(sol.maximumGain('cdbcbbaaabab', 4, 5))  # 19
print(sol.maximumGain('cdbcbbaaabab', 5, 4))  # 18
print(sol.maximumGain('aabbaaxybbaabb', 5, 4))  # 20
print(sol.maximumGain('aabbaaxybbaabb', 4, 5))  # 20
print(sol.maximumGain("paaaabdbabfbybbbtaaab", 8132, 1776))  # 24396
print(sol.maximumGain("cbaabwbbbabbwaaq", 4074, 9819))  # 23712
print(sol.maximumGain("aaaaaaaaaaaaaabbbbbbbbbbbbb", 123, 3495))  # 1599
print(
    sol.maximumGain(
        "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha",
        1926, 4320))  # 112374
