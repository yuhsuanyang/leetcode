//no. 1903
#include <string>
using namespace std;

class Solution {
public:
    string largestOddNumber(string num) {
      int largest_index;
      for(int i = num.length() - 1; i >= 0; i--){
        if (int(num[i] - '0') % 2){
          largest_index = i;
          break;
        }
      }
      if(largest_index == 0 & !int(num[0] - '0') % 2){
        return "";
      }
      return num.substr(0, largest_index+1);
    }
};
