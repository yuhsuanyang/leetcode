# no.1980
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        for i in range(length):
            bin_str = nums[i]
            for j in range(length):
                can = "0" if bin_str[j] == "1" else "1"
                can = bin_str[:j] + can + bin_str[j+1:]
                if can not in nums[i:]:
                    return can
