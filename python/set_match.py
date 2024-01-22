#no. 645

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        n = len(nums)
        counter = {i + 1: 0 for i in range(n)}
        for i in nums:
            counter[i] += 1
        for i in range(n):
            if counter[i + 1] == 2:
                ans[0] = i + 1
            elif counter[i + 1] == 0:
                ans[1] = i + 1
        return ans
