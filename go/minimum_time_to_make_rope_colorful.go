// no.1578
func minCost(colors string, neededTime []int) int {
	cost := 0
	max_time := neededTime[0]
	for i := 1; i < len(neededTime); i++ {
		if colors[i] == colors[i-1] {
			if neededTime[i] > max_time {
				cost += max_time
				max_time = neededTime[i]
			} else {
				cost += neededTime[i]
			}
		} else {
			max_time = neededTime[i]
		}
	}
	return cost
}
