//no. 1287
func findSpecialInteger(arr []int) int {
    if len(arr) == 1{
        return arr[0]
    }
    threshold := len(arr) / 4
    count := 1
    curr := arr[0]
    for i := 1; i < len(arr); i++{
        if arr[i] == curr{
            count ++
        }else{
            count = 1
            curr = arr[i]
        }
        if count > threshold{
            return curr
        }
    }
    return 0
}
