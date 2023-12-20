# no. 2706
class Solution:
    def get_min(self, nums):
        min_index = 0
        min_ = nums[min_index]
        for i in range(min_index + 1, len(nums)):
            if nums[i] < min_:
                min_ = nums[i]
                min_index = i
        return min_, min_index

    def buyChoco(self, prices: List[int], money: int) -> int:
        first_price, first_index = self.get_min(prices)
        if first_price >= money:
            return money
        del prices[first_index]
        second_price, _ = self.get_min(prices)
        change = money - first_price - second_price
        return change if change >= 0 else money
