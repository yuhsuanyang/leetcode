// no. 2610
func findMatrix(nums []int) [][]int {
	var ans [][]int
	curr_map := make(map[int]int)
	var row int
	for _, n := range nums {
		row = curr_map[n]
		if row > len(ans)-1 {
			new_row := []int{n}
			ans = append(ans, new_row)
		} else {
			ans[row] = append(ans[row], n)
		}
		curr_map[n] = row + 1
	}
	return ans
}
