# no. 2244
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        task_levels = {}
        n_rounds = 0
        for task in tasks:
            task_levels[task] = task_levels.get(task, 0) + 1
        for key, value in task_levels.items():
            if self.get_needed_round(value) == -1:
                return -1
            else:
                n_rounds += self.get_needed_round(value)
        return n_rounds

    def get_needed_round(self, n_task):
        if n_task == 1:
            return -1
        if n_task % 3 == 0:
            return n_task // 3
        else:
            return n_task // 3 + 1


sol = Solution()
print(sol.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(sol.minimumRounds([2, 3, 3]))
