# no. 2133
class Solution:
    def checkValid(self, matrix) -> bool:
        size = len(matrix)
        rows = [[] for _ in range(size)]
        columns = [[] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if matrix[i][j] not in rows[i]:
                    rows[i].append(matrix[i][j])
                if matrix[i][j] not in columns[j]:
                    columns[j].append(matrix[i][j])
        for i in range(size):
            if (len(rows[i]) != size) or (len(columns[i]) != size):
                return False
        return True

sol = Solution()
print(sol.checkValid([[1,2,3],[3,1,2],[2,3,1]]))
print(sol.checkValid([[1,1,1],[1,2,3],[1,2,3]]))
