// no.2264
#include <string>
using namespace std;

class Solution {
public:
    string largestGoodInteger(string num) {
        char can = num[0];
        char ans = ' ';
        int count = 1;
        for(int i = 1; i < num.size(); i++){
            if(num[i] == can){
                count ++;
            }else{
               count = 1;
               can = num[i]; 
            }
            if(count == 3 & ans < can){
                ans = can;
            }
            
        }
        return ans == ' ' ? "" : string(3, ans);
    }
};
