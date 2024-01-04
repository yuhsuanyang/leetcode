# no. 2870
class Solution:
    def getMinDeletion(self, num):
        if num <= 3:
            return 1
        total_deletion = 0
        while num > 4:
            if num % 3 == 1:
                num_deletion = num // 3 - 1
            else:
                num_deletion = num // 3
            num -= num_deletion * 3
            total_deletion += num_deletion
        num_deletion = num // 2
        total_deletion += num_deletion
        return total_deletion

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        num_counts = {}
        for i in nums:
            num_counts[i] = num_counts.get(i, 0) + 1
        for i in num_counts:
            if num_counts[i] == 1:
                return -1
            ans += self.getMinDeletion(num_counts[i])
        return ans
            
