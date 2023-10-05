# no. 983
class Solution(object):
    def mincostTickets(self, days, costs, verbose=False):
        #        type_of_tickets = [1, 7, 30]
        dp = [0]
        offset_days = days[0] - 1
        for i in range(1, days[-1] - offset_days + 1):
            if (i + offset_days) in days:
                dp.append(
                    min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1],
                        dp[max(0, i - 30)] + costs[2]))
            else:
                dp.append(dp[i - 1])
        if verbose:
            for i, j in enumerate(dp):
                print(f"day {i}", ':', j)
        return dp[-1]


sol = Solution()
sol.mincostTickets([4, 8, 15, 25, 36], [2, 7, 15])  # 10
sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])  # 10
sol.mincostTickets([i for i in range(1, 11)] + [30, 31], [2, 7, 15],
                   True)  # 10
