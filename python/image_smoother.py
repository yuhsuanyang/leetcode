# no.611
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n_rows = len(img)
        n_cols = len(img[0])
        ans = []
        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                sum_ = img[i][j]
                counter = 1
                for k in [-1, 1]:
                    if j + k >= 0 and j + k < n_cols:
                        sum_ += img[i][j + k]
                        counter += 1
                        if i + k >= 0 and i + k < n_rows:
                            sum_ += img[i + k][j + k]
                            counter += 1
                    if i - k >= 0 and i - k < n_rows:
                        sum_ += img[i - k][j]
                        counter += 1
                        if j + k >= 0 and j + k < n_cols:
                            sum_ += img[i - k][j + k]
                            counter += 1
                row.append(sum_ // counter)
            ans.append(row)
        return ans
