// no. 451
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
  vector<int> heap;
  void swap(int i, int j) {
    int temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
  }
  string frequencySort(string s) {
    vector<int> counter;
    for (int i = 48; i <= 122; i++) {
      counter.push_back(0);
    }
    for (char c : s) {
      counter[int(c) - 48]++;
    }
    vector<int> non_zero;
    for (int i = 0; i < counter.size(); i++) {
      if (counter[i] != 0) {
        non_zero.push_back(i);
      }
    }
    heap.push_back(non_zero[0]);
    for (int i = 1; i < non_zero.size(); i++) {
      heap.push_back(non_zero[i]);
      int k = i;
      while ((k > 0) & (counter[heap[k]] > counter[heap[(k - 1) / 2]])) {
        swap((k - 1) / 2, k);
        k = (k - 1) / 2;
      }
    }
    string ans;
    while (heap.size()) {
      for (int j = 0; j < counter[heap[0]]; j++) {
        ans += char(heap[0] + 48);
      }
      heap.front() = heap.back();
      heap.pop_back();
      int k = 0;
      int swap_node;
      while (k * 2 + 2 < heap.size()) {
        if (counter[heap[k * 2 + 1]] > counter[heap[k * 2 + 2]]) {
          swap_node = k * 2 + 1;
        } else {
          swap_node = k * 2 + 2;
        }
        if (counter[heap[k]] < counter[heap[swap_node]]) {
          swap(k, swap_node);
          k = swap_node;
        } else {
          break;
        }
      }
      if (heap.size() == 2) {
        if (counter[heap[0]] < counter[heap[1]]) {
          swap(0, 1);
        }
      }
    }
    return ans;
  }
};
