// no. 229
#include <map>
using namespace std;

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        map<int, int> counter_map;
        int threshold = nums.size() / 3;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            int curr_count = counter_map[num];
            counter_map[num] = curr_count + 1;
        }
        for (map<int, int>::iterator it = counter_map.begin(); it != counter_map.end(); it++){
            if (it->second > threshold){
                result.push_back(it->first);
            }
        }
        return result;
    }
};
