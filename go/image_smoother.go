// no. 661
func imageSmoother(img [][]int) [][]int {
	n_rows := len(img)
	n_cols := len(img[0])
	var ans [][]int
	index := []int{-1, 1}
	for i := 0; i < n_rows; i++ {
		var row []int
		for j := 0; j < n_cols; j++ {
			sum := img[i][j]
			count := 1
			for _, k := range index {
				if (j+k >= 0) && (j+k < n_cols) {
					sum += img[i][j+k]
					count++
					if (i+k >= 0) && (i+k < n_rows) {
						sum += img[i+k][j+k]
						count++
					}
				}
				if (i-k >= 0) && (i-k < n_rows) {
					sum += img[i-k][j]
					count++
					if (j+k >= 0) && (j+k < n_cols) {
						sum += img[i-k][j+k]
						count++
					}
				}
			}
			row = append(row, sum/count)
		}
		ans = append(ans, row)
	}
	return ans
}
