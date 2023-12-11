# no. 1287
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        threshold = len(arr) // 4
        count = 1
        curr = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == curr:
                count += 1
            else:
                curr = arr[i]
                count = 1
            if count > threshold:
                return curr
