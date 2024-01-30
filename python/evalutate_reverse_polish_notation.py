#no. 150

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def get_operate_nums():
            num1 = stack.pop()
            num2 = stack.pop()
            return num1, num2

        for i in tokens:
            if i == '+':
                num1, num2 = get_operate_nums()
                stack.append(num1 + num2)
            elif i == '-':
                num1, num2 = get_operate_nums()
                stack.append(num2 - num1)
            elif i == '*':
                num1, num2 = get_operate_nums()
                stack.append(num1 * num2)
            elif i == '/':
                num1, num2 = get_operate_nums()
                q = int(num2 / num1)
                stack.append(q)
            else:
                stack.append(int(i))
        return stack[0]
