# no. 1582
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n_cols = len(mat[0])
        n_rows = len(mat)
        one_row, one_col = [], []
        row_dict, col_dict = {}, {}
        for i in range(n_rows):
            for j in range(n_cols):
                if mat[i][j]:
                    one_row.append(i)
                    one_col.append(j)
                    row_dict[i] = row_dict.get(i, 0) + 1
                    col_dict[j] = col_dict.get(j, 0) + 1
        ans = 0
        for i in range(len(one_row)):
            if row_dict[one_row[i]] == 1 and col_dict[one_col[i]] == 1:
                ans += 1
        return ans


