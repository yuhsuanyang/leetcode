# no. 2149
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_part, neg_part = [], []
        for i in nums:
            if i > 0:
                pos_part.append(i)
            else:
                neg_part.append(i)
        for i in range(len(nums)):
            if i % 2:
                nums[i] = neg_part[i // 2]
            else:
                nums[i] = pos_part[i // 2]
        return nums
