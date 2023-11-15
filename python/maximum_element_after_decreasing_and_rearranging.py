# no.1846
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        arr.sort()
        arr[0] = 1
        arr[-2] = min(arr[-2], len(arr) - 1)
        if arr[-1] == arr[-2]:
            return arr[-2]
        else:
            return arr[-2] + 1
