//no. 1716
func sum_of_days(start int, n_days int) int{
    return (2 * start + n_days - 1) * n_days / 2
}
func totalMoney(n int) int {
    var week int = 1
    var total_money int = 0
    for{
        if n <= 7{
            break
        }
        total_money += sum_of_days(week, 7)
        n -= 7
        week++
    }
    total_money += sum_of_days(week, n)
    return total_money
}
