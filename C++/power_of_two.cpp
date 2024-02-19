// no. 231

class Solution {
public:
  bool isPowerOfTwo(int n) {
    if (n <= 0) {
      return false;
    }
    if (n <= 2) {
      return true;
    }
    if (n % 2) {
      return false;
    }
    bool ans = isPowerOfTwo(n / 2);
    return ans;
  }
};
