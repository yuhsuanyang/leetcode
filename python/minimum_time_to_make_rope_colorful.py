#no. 1578
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        max_time = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                if neededTime[i] > max_time:
                    cost += max_time
                    max_time = neededTime[i]
                else:
                    cost += neededTime[i]
            else:
                max_time = neededTime[i]
        return cost
