// no. 1624
func maxLengthBetweenEqualCharacters(s string) int {
	ans := -1
	for i := 0; i < len(s); i++ {
		for j := len(s) - 1; j > 0; j-- {
			if s[i] == s[j] {
				length_between_equal := j - i - 1
				if length_between_equal > ans {
					ans = length_between_equal
				}
				break
			}
		}
	}
	return ans
}
