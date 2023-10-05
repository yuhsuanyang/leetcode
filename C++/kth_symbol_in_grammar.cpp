// no. 779
#include <iostream>
using namespace std;

class Solution{
    public:
        int kthGrammar(int n, int k) {
            if(n == 1){
                return 0;
            }          
            int prev_k = kthGrammar(n-1, int((k+1)/2));
            if (prev_k){ // 1 -> 10
                return k % 2;
            }else{ // 0 -> 01
                return (k + 1) % 2;
            }
            
        }
};

int main(){
    Solution sol;
    cout << sol.kthGrammar(4, 3);
}
