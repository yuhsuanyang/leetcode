# no. 2087
class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
       # -1 for walk up, 1 for walk down
        row_step = -1 if startPos[0] > homePos[0] else 1
        # -1 for walk left, 1 for walk right
        col_step = -1 if startPos[1] > homePos[1] else 1
        row_path = [rowCosts[i + row_step] for i in range(startPos[0], homePos[0], row_step)]
        col_path = [colCosts[i + col_step] for i in range(startPos[1], homePos[1], col_step)]
        return sum(row_path) + sum(col_path)       

solution = Solution()
print(solution.minCost([1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]))
print(solution.minCost([2, 3], [1, 0], [5, 4, 3], [8, 2, 6, 7]))
print(solution.minCost([0, 0], [0, 0], [5], [26]))
