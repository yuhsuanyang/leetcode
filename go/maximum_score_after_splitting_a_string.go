// no. 1422
func maxScore(s string) int {
	max_score := 0
	var ones []int
	for i := 0; i < len(s)-1; i++ {
		if s[i] == '1' {
			ones = append(ones, i)
		}
	}
	ones = append(ones, len(s)-1)
	for i := 0; i < len(ones); i++ {
		j := ones[i]
		if j == 0 {
			continue
		}
		right_score := len(ones) - i
		if s[len(s)-1] == '0' {
			right_score--
		}
		left_score := j - i
		total := left_score + right_score
		if total > max_score {
			max_score = total
		}
	}
	return max_score
}
