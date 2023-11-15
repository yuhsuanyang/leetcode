//no. 1846
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        if (arr.size() == 1){
            return 1;
        }
        sort(arr.begin(), arr.end());
        arr[0] = 1;
        const int arr_size = arr.size() - 1;
        const int max_can = arr[arr.size() - 2];
        arr[arr.size() - 2] = min(max_can, arr_size);
        if (arr[arr.size() - 1] == arr[arr.size() - 2]){
            return arr[arr.size() - 1];
        }else{
            return arr[arr.size() - 2] + 1;
        }
    }
};
