// no.2785
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string vowels;
    Solution(){
        vowels = "AEIOUaeiou";
    }
    bool checkVowel(char s){
        for(int i = 0; i < vowels.length(); i++){
            if(s == vowels[i]){
                return true;
            }
        }
        return false;
    }
    string sortVowels(string s) {
        vector<int> vowel_pos;
        vector<char> vs;
        for(int i = 0; i < s.length(); i++){
            if (checkVowel(s[i])){
                vs.push_back(s[i]);
                vowel_pos.push_back(i);
            }
        }
        if(vowel_pos.size()){
            sort(vs.begin(), vs.end());
            for (int i = 0; i < vowel_pos.size(); i++){
                s[vowel_pos[i]] = vs[i];
            }
        }
        return s;
    }
};
