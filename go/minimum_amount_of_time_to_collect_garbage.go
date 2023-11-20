// no.2391
func calcualate_time(sort_of_garbage []int, travel []int) int{
    garbage_time := len(sort_of_garbage)
    if garbage_time != 0{
        start := 0
        end := sort_of_garbage[len(sort_of_garbage)- 1];
        for i := start; i < end; i++{
            garbage_time += travel[i]
        }
        return garbage_time
    }else{
        return 0
    }
}
func garbageCollection(garbage []string, travel []int) int {
    var glass []int
    var metal []int
    var paper []int
    for i, g := range garbage{
        for _, j := range g{
            switch j{
                case 'G':
                glass = append(glass, i)
                case 'M':
                metal = append(metal, i)
                case 'P':
                paper = append(paper, i)
            }
        }
    }
    glass_time := calcualate_time(glass, travel)
    metal_time := calcualate_time(metal, travel)
    paper_time := calcualate_time(paper, travel)
    return glass_time + metal_time + paper_time


}
