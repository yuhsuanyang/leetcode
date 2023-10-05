# no. 50
class Solution:
    def __init__(self):
        self.cache = {0: 1}

    def myPow(self, x:float, n: int) -> float:
        self.cache[1] = x
        if x:
            self.cache[-1] = 1 / x
        if n in self.cache:
            return self.cache[n]
        if n % 2 == 0:
            self.cache[n] = self.myPow(x, n/2) * self.myPow(x, n/2)
        else:
            self.cache[n] = x * self.myPow(x, (n-1)/2) * self.myPow(x, (n-1)/2)
        return self.cache[n]
