// no. 1436

func destCity(paths [][]string) string {
	start, end := paths[0][0], paths[0][1]
	paths = paths[1:]
	for len(paths) != 0 {
		for i := 0; i < len(paths); i++ {
			if paths[i][0] == end {
				end = paths[i][1]
				paths = append(paths[:i], paths[i+1:]...)
				break
			}
		}
		for i := 0; i < len(paths); i++ {
			if paths[i][1] == start {
				start = paths[i][0]
				paths = append(paths[:i], paths[i+1:]...)
				break
			}
		}
	}
	return end
}
