//no. 1877
import "sort"
func minPairSum(nums []int) int {
    sort.Slice(nums, func(i, j int) bool {
            return nums[i] < nums[j]
    })
    left := 0
    right := len(nums) - 1
    var pair_sum []int
    for{
        if(left < right){
            sum := nums[left] + nums[right]
            pair_sum = append(pair_sum, sum)
            left += 1
            right -= 1
        }else{
            break
        }
    }
    sort.Slice(pair_sum, func(i, j int) bool {
            return pair_sum[i] < pair_sum[j]
    })
    return pair_sum[len(pair_sum) - 1]
}
