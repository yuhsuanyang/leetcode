# no. 1716
class Solution:
    def sum_of_days(self, start, n_days):
        return (2 * start + n_days - 1) * n_days / 2

    def totalMoney(self, n: int) -> int:
        week = 1
        total_money = 0
        while(n > 7):
            total_money += self.sum_of_days(week, 7)
            n -= 7
            week += 1
        total_money += self.sum_of_days(week, n)
        return int(total_money)
