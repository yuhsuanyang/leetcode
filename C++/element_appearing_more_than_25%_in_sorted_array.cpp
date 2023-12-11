//no. 1287
#include<vector>
using namespace std;
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        if(arr.size() == 1){
            return arr[0];
        }
        int threshold = arr.size() / 4;
        int count = 1;
        int curr = arr[0];
        for(int i = 1; i < arr.size(); i++){
            if(arr[i] == curr){
                count++;
            }else{
                curr = arr[i];
                count = 1;
            }
            if(count > threshold){
                return curr;
            }
        }
        return 0;
    }
};
