# no. 2264
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        can = num[0]
        counter = 1
        ans = ''
        for i in num[1:]:
            if can == i:
                counter += 1
            else:
                can = i
                counter = 1
            if counter == 3 and ans < can:
                ans = can
        return ans * 3 if ans else ans
