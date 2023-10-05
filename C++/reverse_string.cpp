#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution{
    public:
        void reverseString(vector<char> & s, int start=0, int end=0){
            if (end == 0){
                end = s.size() - 1;
            }
            if (start >= end){
                return;
            };
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            reverseString(s, start+1, end-1);
        }
};

int main()
{
    string s = "hello";
    vector <char> v(s.begin(), s.end());
    Solution sol;
    sol.reverseString(v);
    for (int i=0;i<v.size();i++){
        cout << v[i] << " ";
    }
    return 0;
}
