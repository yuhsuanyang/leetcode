# no. 189
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        optimize_step = k % len(nums)
        split_point = len(nums) - optimize_step
        new_nums = nums[split_point:] + nums[:split_point]
        for i in range(len(nums)):
           nums[i] = new_nums[i]
