//no. 50
#include<iostream>
#include<map>
using namespace std;

class Solution {
public:
    map<int, double> cache;
    Solution(){
        cache[0] = 1;
    }
    double myPow(double x, int n) {
        cache[1] = x;
        if (x != 0){
            cache[-1] = 1/x;
        }
        map<int, double>::iterator it;
        it = cache.find(n);
        if (it != cache.end()){
            return cache[n];
        }
        if (n%2 == 0){
            cache[n] = myPow(x, n/2) * myPow(x, n/2);
        }else{

            cache[n] = x * myPow(x, (n - 1)/2) * myPow(x, (n - 1)/2);
        }
        return cache[n];
    }
};

int main(){
    Solution sol;
    cout<< sol.myPow(34, -3) << endl;
    return 0;
}
