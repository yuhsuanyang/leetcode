// no. 2706

func getMin(nums []int) (int, int) {
	min_index := 0
	min_ := nums[min_index]
	for i := min_index + 1; i < len(nums); i++ {
		if nums[i] < min_ {
			min_index = i
			min_ = nums[min_index]
		}
	}
	return min_, min_index
}

func buyChoco(prices []int, money int) int {
	first_price, i := getMin(prices)
	if first_price >= money {
		return money
	}
	prices = append(prices[:i], prices[i+1:]...)
	second_price, _ := getMin(prices)
	change := money - first_price - second_price
	if change >= 0 {
		return change
	} else {
		return money
	}
}
