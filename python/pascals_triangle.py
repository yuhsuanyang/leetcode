# no.118
class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        triangle = [[1], [1, 1]]
        for i in range(numRows-2):
            row = [1]
            last_row = triangle[-1]
            for j in range(len(last_row)-1):
                row.append(last_row[j]+last_row[j+1])
            row.append(1)
            triangle.append(row)
        return triangle

sol = Solution()
print(sol.generate(2))


