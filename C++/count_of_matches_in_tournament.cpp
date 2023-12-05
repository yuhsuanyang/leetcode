// no. 1688
class Solution {
public:
    int numberOfMatches(int n) {
        int matches = 0;
        int match_this_round = 0;
        while(n >= 2){
            match_this_round = n / 2;
            matches += match_this_round;
            n -= match_this_round;
        }
        return matches;
    }
};
