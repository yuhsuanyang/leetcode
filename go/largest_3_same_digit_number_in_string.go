//no. 2264
import(
  "strings"
)

func largestGoodInteger(num string) string {
    var can = num[0]
    var ans = byte(0)
    var count = 1
    for i := 1; i < len(num); i++{
        if can == num[i] {
            count ++
        }else{
            can = num[i]
            count = 1
        }
        if (count == 3) && (ans < can){
            ans = can
        }
    }
    str_ans := string(ans)
    if ans == byte(0){
        return ""
    }else{
        return strings.Repeat(str_ans, 3)
    }
}
