//no. 1980

func is_in_arr(s string, nums []string) bool{
    for _, i := range nums{
        if i == s{
            return true
        }
    }
    return false
}

func findDifferentBinaryString(nums []string) string {
    length := len(nums)
    var can string
    for i := 0; i < length; i++{
        bin_str := nums[i]
        for j := 0; j < length; j++{
            if bin_str[j] == '0'{
                can = "1"
            }else{
                can = "0"
            }
            can = bin_str[:j] + can + bin_str[j+1:]
            if !is_in_arr(can, nums){
                return can
            }
        }
    }
    return can
}
