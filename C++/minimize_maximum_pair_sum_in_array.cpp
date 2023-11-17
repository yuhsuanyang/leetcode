//no. 1877
#include <vector>
using namespace std;
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int left = 0;
        int right = nums.size() - 1;
        vector<int> pair_sum; 
        while(left < right){
            pair_sum.push_back(nums[left] + nums[right]);
            left += 1;
            right -= 1;
        }
        int max = 0;
        for (int i = 0; i < pair_sum.size(); i++){
            if (pair_sum[i] > max){
                max = pair_sum[i];
            }
        }
        return max;
    }
};
