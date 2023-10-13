// no. 746
#include <vector>
using namespace std;

class Solution {
    public:
        int minCostClimbingStairs(vector<int>& cost) {
            cost.push_back(0);
            vector<int> dp;
            dp.push_back(cost[0]);
            dp.push_back(cost[1]);
            for (int i = 2; i < cost.size(); i++){
                int min_cost_state = min(dp[i-1], dp[i-2]);
                dp.push_back(min_cost_state + dp[i]);
            }
            return dp[cost.size() - 1]; 
        }
};


