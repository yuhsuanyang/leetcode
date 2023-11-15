//no.1846
import "sort"

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
    if (len(arr) == 1){
        return 1
    }
    sort.Slice(arr, func(i, j int)bool {
        return arr[i] < arr[j]
    })
    arr[0] = 1
    arr[len(arr)-2] = min(arr[len(arr)-2], len(arr) - 1)
    if (arr[len(arr)-2] == arr[len(arr)-1]){
        return arr[len(arr)-1]
    }else{
        return arr[len(arr)-2] + 1
    }
}
