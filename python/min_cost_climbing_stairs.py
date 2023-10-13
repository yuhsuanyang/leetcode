# no.746

from typing import List

class Solution:
    def helper(self, cost, n):
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = min(self.helper(cost, n - 1), self.helper(cost, n - 2)) + cost[n]
        return self.cache[n]
    
    def minCostClimbingStairs_recur(self, cost: List[int]) -> int:
        self.cache = {}
        self.cache[0] = cost[0]
        self.cache[1] = cost[1]
        cost.append(0)
        return self.helper(cost, len(cost) - 1)

    def minCostClimbingStairs_dp(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            min_cost_state = min(dp[i - 1], dp[i - 2])
            dp.append(min_cost_state + cost[i])
        print(dp)
        return dp[-1]
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs_recur([10, 15, 20]))
    print(sol.minCostClimbingStairs_recur([1,100,1,1,1,100,1,1,100,1]))
    print(sol.minCostClimbingStairs_dp([10, 15, 20]))
    print(sol.minCostClimbingStairs_dp([1,100,1,1,1,100,1,1,100,1]))
