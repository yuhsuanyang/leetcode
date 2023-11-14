//no. 1930
func countPalindromicSubsequence(s string) int {
    counter := make(map[byte][]int)
    for i := 0; i < len(s); i++{
        counter[s[i]] = append(counter[s[i]], i)
    }
    var ans = 0
    pan := make(map[byte]bool)
    for k := range(counter){
        var start = counter[k][0] + 1
        var end = counter[k][len(counter[k]) - 1]
        for i := start; i < end; i++{
            pan[s[i]] = true
        }
        ans += len(pan)
        clear(pan)
    }
    return ans
}
