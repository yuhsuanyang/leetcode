// no. 1582
func numSpecial(mat [][]int) int {
	n_cols := len(mat[0])
	n_rows := len(mat)
	var ones [][]int
	row_map := make(map[int]int)
	col_map := make(map[int]int)
	ans := 0
	for i := 0; i < n_rows; i++ {
		for j := 0; j < n_cols; j++ {
			if mat[i][j] == 1 {
				ones = append(ones, []int{i, j})
				row_map[i] += 1
				col_map[j] += 1
			}
		}
	}
	for _, pos := range ones {
		if (row_map[pos[0]] == 1) && (col_map[pos[1]] == 1) {
			ans++
		}
	}
	return ans
}
