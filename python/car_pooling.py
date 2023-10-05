# no. 1094
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        routes = {i: 0 for i in range(1000)}
        for num_passengers, start, end in trips:
            for i in range(start, end):
                routes[i] += num_passengers
                if routes[i] > capacity:
                    return False
        return True


sol = Solution()
print(sol.carPooling([[2, 1, 5], [3, 3, 7]], 4))  # false
print(sol.carPooling([[2, 1, 5], [3, 3, 7]], 5))  # false
print(
    sol.carPooling([[6, 6, 7], [5, 1, 5], [1, 4, 7], [6, 3, 7], [1, 1, 3],
                    [3, 1, 7], [8, 4, 6], [10, 2, 9], [8, 6, 7]], 33))  # false
print(sol.carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13))  # true
