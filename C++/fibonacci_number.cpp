//no. 505
#include<iostream>
#include <map>
using namespace std;

class Solution {
    public:
    map<int, int> cache;
    Solution(){ 
        cache[0] = 0;
        cache[1] = 1;
    }
    int fib(int n) {
        map<int, int>:: iterator it;
        it = cache.find(n);
        if (it != cache.end()){
            return it->second;
        }
        int ans = fib(n-1) + fib(n-2);
        cache[n] = ans;
        return ans;
                        
    }
};

int main(){
    Solution sol;
    int k;
    cout << "enter question, k=";
    cin >> k;
    cout << "answer: " << sol.fib(k) << endl;
    return 0;
}
