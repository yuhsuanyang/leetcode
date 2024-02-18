#no. 8
class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        nums = []
        sign = 1
        start = 0
        upper_bound = (2 ** 31) - 1
        lower_bound = (-1) * 2 ** 31
        for i in range(len(s)):
            if s[i] != ' ':
                start = i
                break
        for i in range(start, len(s)):
            if ord(s[i]) <= 57 and ord(s[i]) >= 48: # 0-9
                nums.append(s[i])
            elif s[i] == '-' or s[i] == '+':
                if not nums:
                    nums.append(s[i])
                else:
                    break
            else:
                break
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] == '-':
                sign = (-1)
                continue
            elif nums[i] == '+':
                continue
            digit = int(nums[i])
            if((ans > upper_bound // 10) or ((ans == upper_bound // 10) and digit > 7)):
                if sign == 1:
                    return upper_bound
                else:
                    return lower_bound
            ans = ans * 10 + digit
        return sign * ans
