# no. 123
class Solution(object):
    def maxProfit(self, prices):

        n = len(prices)

        l_profits = [0] * n #從左邊看過去 最多能獲利多少
        r_profits = [0] * n #從右邊看過來 最多能獲利多少
        l_min = prices[0]
        r_max = prices[-1]
        
        for i in range(1, n):
            if prices[i] < l_min:
                l_min = prices[i]

            l_profits[i] = max(l_profits[i-1], prices[i] - l_min)

            if prices[n-i-1] > r_max:
                r_max = prices[n-i-1]

            r_profits[n-i-1] = max(r_profits[n-i], r_max - prices[n-i-1])
        
        #print(l_profits)
        #print(r_profits)
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, r_profits[i] + l_profits[i])

        return max_profit
           
        
sol = Solution()
print(sol.maxProfit([3,3,5,0,0,3,1,4])) #6
print(sol.maxProfit([3,3,5,0,0,2,1,4])) #6
print(sol.maxProfit([1,2,3,4,5])) #4
print(sol.maxProfit([7,6,4,3,1])) #0
print(sol.maxProfit([1])) #0
print(sol.maxProfit([6,1,3,2,4,7])) #7
print(sol.maxProfit([4,5,3,11,4,15,7,8])) #19
