# no. 70
class Solution(object):
    def __init__(self):
        self.ways = {1: 1, 2: 2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ways = [1, 2]
        for i in range(2, n):
            ways.append(ways[i - 1] + ways[i - 2])
        return ways[-1]

    def climbStairs_recursive(self, n):
        if n in self.ways:
            return self.ways[n]

        else:
            self.ways[n] = self.climbStairs_recursive(n - 1) + self.climbStairs_recursive(n - 2)
            return self.ways[n]

if __name__ == '__main__':
    sol = Solution()
    for i in range(1, 46):
        print(sol.climbStairs(i))
