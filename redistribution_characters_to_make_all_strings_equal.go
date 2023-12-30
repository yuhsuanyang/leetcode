// no. 1897

func makeEqual(words []string) bool {
	char_map := make(map[rune]int)
	for _, w := range words {
		for _, c := range w {
			char_map[c]++
		}
	}
	for _, i := range char_map {
		if i%len(words) != 0 {
			return false
		}
	}
	return true
}
