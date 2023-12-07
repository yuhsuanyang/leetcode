# no. 1903

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
          if int(num[i]) % 2:
            break
        if i == 0:
          if int(num[i]) % 2:
            return num[0]
          else:
            return ""
        return num[0:i+1]
