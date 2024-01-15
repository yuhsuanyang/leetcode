# no. 2225
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_dict = [0] * 100000
        for match in matches:
            winner = match[0] - 1
            loser = match[1] - 1
            if lose_dict[winner] == 0:
                lose_dict[winner] = -1
            if lose_dict[loser] == -1:
                lose_dict[loser] = 1
            else:
                lose_dict[loser] += 1
            
        ans = [[], []]
        for i in range(len(lose_dict)):
            if lose_dict[i] == 1:
                ans[1].append(i + 1)
            elif lose_dict[i] == -1:
                ans[0].append(i + 1)
        return ans
