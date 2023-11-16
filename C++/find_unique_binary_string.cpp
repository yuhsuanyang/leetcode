//no. 1980
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool is_in_list(string s, vector<string>& v){
        for(int i = 0; i < v.size(); i++){
            if (v[i] == s){
                return true;
            }
        }
        return false;
    }
    string findDifferentBinaryString(vector<string>& nums) {
        int length = nums.size();
        string can;
        for (int i = 0; i < length; i++){
            string bin_str = nums[i];
            for (int j = 0; j < length; j++){
                if(bin_str[j] == '1'){
                    can = "0";
                }else{
                    can = "1";
                }
                can = bin_str.substr(0, j) + can + bin_str.substr(j+1, length);
                if (!is_in_list(can, nums)){
                    return can;
                }  
            }
        }
        return can;
    }
};
