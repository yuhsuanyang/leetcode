// no. 380
#include <cstdlib>
#include <vector>
using namespace std;

class RandomizedSet {
public:
  vector<int> num_set;
  RandomizedSet() {}

  bool insert(int val) {
    for (int i : num_set) {
      if (i == val) {
        return false;
      }
    }
    num_set.push_back(val);
    return true;
  }

  bool remove(int val) {
    for (int i = 0; i < num_set.size(); i++) {
      if (num_set[i] == val) {
        num_set.erase(num_set.begin() + i);
        return true;
      }
    }
    return false;
  }

  int getRandom() {
    int min = 0;
    int max = num_set.size();
    int rand_index = rand() % (max - min);
    return num_set[rand_index];
  }
};
