func numberOfMatches(n int) int {
    matches := 0
    var match_this_round int
    for{
        if n < 2{
            break
        }
        match_this_round = n / 2
        matches += match_this_round
        n -= match_this_round
    }
    return matches
}
