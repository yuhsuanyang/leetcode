# no. 1688
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while(n >= 2):
            match_this_round = n // 2
            matches += match_this_round
            n -= match_this_round
        return matches
