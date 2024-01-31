# no. 55
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        appoarchable = [0 for _ in range(len(nums))]
        appoarchable[0] = 1
        for i in range(len(nums)):
            if appoarchable[-1]:
                return 1
            if appoarchable[i]:
                for k in range(i + 1, i + nums[i] + 1):
                    if k >= len(nums):
                        break
                    if not appoarchable[k]:
                        appoarchable[k] = 1
        return appoarchable[-1]


