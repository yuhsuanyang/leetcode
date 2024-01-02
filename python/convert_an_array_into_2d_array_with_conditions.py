# no. 2610
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_row = {}
        for n in nums:
            row = curr_row.get(n, 0)
            if row > len(ans) - 1:
                ans.append([n])
            else:
                ans[row].append(n)
            curr_row[n] = row + 1
        return ans

