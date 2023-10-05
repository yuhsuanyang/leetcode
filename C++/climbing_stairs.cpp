// no. 70
#include <iostream>
#include <map>
using namespace std;

class Solution{
    public:
        map<int, int> cache;
        Solution(){
            cache[0] = 0;
            cache[1] = 1;
        }
        int climbStairs(int n){
            map<int, int>::iterator it;
            it = cache.find(n);
            if (it != cache.end()){
                return it->second;
            }
            int ans = climbStairs(n-1) + climbStairs(n-2);
            cache[n] = ans;
            return ans;
        }
};
