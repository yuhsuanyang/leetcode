// no. 2125
func countLights(s string) int {
	ans := 0
	for _, c := range s {
		if c == '1' {
			ans++
		}
	}
	return ans
}

func numberOfBeams(bank []string) int {
	var ans, top, down int
	for _, row := range bank {
		n_row_lights := countLights(row)
		if n_row_lights != 0 {
			if top == 0 {
				top = n_row_lights
			} else if down == 0 {
				down = n_row_lights
				ans += top * down
				top = down
				down = 0
			}
		}
	}
	return ans
}
