// no. 2870

func getMinDeletion(num int) int {
	if num <= 3 {
		return 1
	}
	num_deletion := 0
	total_deletion := 0
	for {
		if num <= 4 {
			break
		}
		if num%3 == 1 {
			num_deletion = num/3 - 1
		} else {
			num_deletion = num / 3
		}
		num -= num_deletion * 3
		total_deletion += num_deletion
	}
	num_deletion = num / 2
	total_deletion += num_deletion
	return total_deletion
}

func minOperations(nums []int) int {
	ans := 0
	num_counts := make(map[int]int)
	for _, i := range nums {
		num_counts[i]++
	}
	for _, n := range num_counts {
		if n == 1 {
			return -1
		}
		ans += getMinDeletion(n)
	}
	return ans
}
