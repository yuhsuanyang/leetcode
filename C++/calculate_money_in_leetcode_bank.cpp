//no. 1716

class Solution {
public:
    int sum_of_days(int start, int n_days){
        return (2 * start + n_days - 1) * n_days / 2;
    }
    int totalMoney(int n) {
        int week = 1;
        int total_money = 0;
        while(n > 7){
            total_money += sum_of_days(week, 7);
            n -= 7;
            week++;
        }
        total_money += sum_of_days(week, n);
        return total_money;
    }
};
