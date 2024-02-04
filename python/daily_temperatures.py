# no. 739
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and (temperatures[stack[-1]] < temperatures[i]):
                    j = stack.pop()
                    answer[j] = i - j
                stack.append(i)
        return answer
