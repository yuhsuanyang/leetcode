// no. 1436
import "fmt"

func destCity(paths [][]string) string {
	var route [][]string
	route = append(route, paths[0])
	paths = paths[1:]
	for len(paths) != 0 {
		fmt.Println(route)
		fmt.Println(paths)
		for i := 0; i < len(paths); i++ {
			if paths[i][0] == route[len(route)-1][1] {
				route = append(route, paths[i])
				paths = append(paths[:i], paths[i+1:]...)
				break
			}
		}
		for i := 0; i < len(paths); i++ {
			if paths[i][1] == route[0][0] {
				tmp := [][]string{paths[i]}
				route = append(tmp, route...)
				paths = append(paths[:i], paths[i+1:]...)
				break
			}
		}
	}
	return route[len(route)-1][1]
}
