# no. 120
# bottom up
class Solution:
    def minimumTotal(self, triangle) -> int:
        dp = [triangle[-1]]
        for i in range(len(triangle)-2, -1, -1):
            dp_new_row = []
            dp_last_row = dp[-1]
            triangle_row = triangle[i]
            for j in range(len(dp_last_row)-1):
                dp_new_row.append(min(dp_last_row[j]+triangle_row[j], dp_last_row[j+1]+triangle_row[j]))
            dp.append(dp_new_row)
        print(dp)
        return dp[-1][0]
            


sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(sol.minimumTotal([[-1],[2,3],[1,-1,-3]])) # -1
print(sol.minimumTotal([[-10]])) # -10
