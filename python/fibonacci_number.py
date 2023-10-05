# no.505
class Solution:
    def __init__(self):
        self.cache = {}

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        elif n in self.cache:
            return self.cache[n]
        else:
            ans = self.fib(n - 1) + self.fib(n - 2)
            self.cache[n] = ans
            return ans
