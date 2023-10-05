class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        row = [1]
        last_row = self.getRow(rowIndex - 1)
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i+1])
        row.append(1)
        return row
