#no. 42
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        ans = 0
        for i in range(1, len(height)):
            while stack and (height[i] > height[stack[-1]]):
                if len(stack) >= 2:
                    ans += (min(height[stack[-2]], height[i]) - height[stack[-1]]) * (i - stack[-2] - 1)
                stack.pop()
            stack.append(i)
        return ans
