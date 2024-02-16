// no. 1481
#include <map>
#include <vector>
using namespace std;
class Solution {
public:
  vector<int> heap;
  void swap(int i, int j) {
    int tmp = heap[i];
    heap[i] = heap[j];
    heap[j] = tmp;
  }
  int findLeastNumOfUniqueInts(vector<int> &arr, int k) {
    map<int, int> counter;
    for (int i : arr) {
      counter[i]++;
    }
    if (k == 0) {
      return counter.size();
    }
    for (map<int, int>::iterator it = counter.begin(); it != counter.end();
         it++) {
      heap.push_back(it->first);
      int j = heap.size() - 1;
      if (j == 0) {
        continue;
      }
      while (counter[heap[j]] < counter[heap[(j - 1) / 2]]) {
        swap(j, (j - 1) / 2);
        j = (j - 1) / 2;
        if (j == 0) {
          break;
        }
      }
    }
    while (k > 0) {
      k -= counter[heap[0]];
      heap[0] = heap.back();
      heap.pop_back();
      int j = 0;
      while (j * 2 + 2 < heap.size()) {
        int child;
        if (counter[heap[j * 2 + 1]] < counter[heap[j * 2 + 2]]) {
          child = j * 2 + 1;
        } else {
          child = j * 2 + 2;
        }
        if (counter[heap[j]] > counter[heap[child]]) {
          swap(j, child);
          j = child;
        } else {
          break;
        }
      }
      if (heap.size() == 2) {
        if (counter[heap[0]] > counter[heap[1]]) {
          swap(0, 1);
        }
      }
    }
    if (k < 0) {
      return heap.size() + 1;
    } else {
      return heap.size();
    }
  }
};
