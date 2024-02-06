// no. 49
#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  map<char, string> dict;
  Solution() {
    string alphabets = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0; i < alphabets.length(); i++) {
      dict[alphabets[i]] = to_string(i);
    }
  }
  string encode(string s) {
    vector<string> seq;
    for (char c : s) {
      seq.push_back(dict[c]);
    }
    sort(seq.begin(), seq.end());
    string result = "";
    for (string num : seq) {
      result += num;
      result += " ";
    }
    return result;
  }
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    map<string, vector<string>> anagrams;
    for (string s : strs) {
      string encoded = encode(s);
      anagrams[encoded].push_back(s);
    }
    vector<vector<string>> ans;
    map<string, vector<string>>::iterator it;
    for (it = anagrams.begin(); it != anagrams.end(); it++) {
      ans.push_back(it->second);
    }
    return ans;
  }
};
