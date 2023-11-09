//no. 1759
import "string"

func countHomogenous(s string) int {
    var ans = 1
    var curr_streak = 1
    const mod = 1e9 + 7
    for i := 0; i < len(s) - 1; i++ {
        if s[i] == s[i + 1]{
            curr_streak += 1
        }else{
            curr_streak = 1
        }
        ans += curr_streak
        ans = ans % mod
    }
    return ans
}
