# no. 35
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target > nums[-1]:  # max: append to the last one
            return len(nums)
        elif target < nums[0]:  # min: insert to the first one
            return 0

        l_key, r_key = 0, len(nums)
        mid = (l_key + r_key) // 2
        while r_key > l_key:
            print(nums[l_key:r_key + 1])
            #            print(mid)
            if nums[mid] < target:
                l_key = mid + 1
            elif nums[mid] > target:
                r_key = mid - 1

            else:
                return mid

            mid = (l_key + r_key) // 2

        if nums[mid] > target:
            return mid
        else:
            return mid + 1


solution = Solution()
print('------------')
print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
print('------------')
print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
print('------------')
print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
print(solution.searchInsert([1, 3, 5, 6], 0))  # 0
print('------------')
print(solution.searchInsert([1], 0))  # 0
print('------------')
print(solution.searchInsert([1, 4, 6, 7, 10], 8))  # 4
print('------------')
print(solution.searchInsert([1, 3], 1))  # 0
