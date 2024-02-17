// no. 1642
#include <vector>
using namespace std;
class Solution {
public:
  vector<int> heap;
  void heap_swap(int i, int j) {
    int tmp = heap[i];
    heap[i] = heap[j];
    heap[j] = tmp;
  }
  void heap_push(int num) {
    heap.push_back(num);
    int k = heap.size() - 1;
    while (heap[k] < heap[(k - 1) / 2]) {
      heap_swap(k, (k - 1) / 2);
      k = (k - 1) / 2;
      if (k <= 0) {
        break;
      }
    }
  }
  int heap_pop() {
    int val = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    int k = 0;
    while (k * 2 + 2 < heap.size()) {
      int child;
      if (heap[k * 2 + 2] < heap[k * 2 + 1]) {
        child = k * 2 + 2;
      } else {
        child = k * 2 + 1;
      }
      if (heap[k] > heap[child]) {
        heap_swap(k, child);
        k = child;
      } else {
        break;
      }
    }
    if (heap.size() == 2) {
      if (heap[0] > heap[1]) {
        heap_swap(0, 1);
      }
      return val;
    }
    return val;
  }
  int furthestBuilding(vector<int> &heights, int bricks, int ladders) {
    for (int i = 1; i < heights.size(); i++) {
      if (heights[i] > heights[i - 1]) {
        int diff = heights[i] - heights[i - 1];
        heap_push(diff);
      }
      if (heap.size() > ladders) {
        bricks -= heap_pop();
      }
      if (bricks < 0) {
        return i - 1;
      }
    }
    return heights.size() - 1;
  }
};
