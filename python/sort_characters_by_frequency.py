# no. 451
class Solution:
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def frequencySort(self, s: str) -> str:
        counter = [0 for _ in range(48, 123)]
        for c in s:
            counter[ord(c) - 48] += 1
        non_zero = [i for i in range(len(counter)) if counter[i]]
        self.heap = [non_zero[0]]
        # construct heap
        for i in range(1, len(non_zero)):
            self.heap.append(non_zero[i])
            k = i
            while (k > 0) and (counter[self.heap[k]] > counter[self.heap[(k - 1) // 2]]): # parent: (k - 1) // 2
                self.swap((k - 1) // 2, k)
                k = (k - 1) // 2
        ans = ""
        # heap pop
        while self.heap:
            ans += chr(self.heap[0] + 48) * counter[self.heap[0]]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            # print(self.heap)
            k = 0
            while k * 2 + 2 < len(self.heap): # child: (k * 2 + 1), (k * 2 + 2)
                if counter[self.heap[k * 2 + 1]] > counter[self.heap[k * 2 + 2]]:
                    swap_node = k * 2 + 1
                else:
                    swap_node = k * 2 + 2
                if counter[self.heap[k]] < counter[self.heap[swap_node]]:
                    self.swap(k, swap_node)
                    k = swap_node
                else:
                    break
                # print(self.heap)
            if len(self.heap) == 2:
                if counter[self.heap[0]] < counter[self.heap[1]]:
                    self.swap(0, 1)
        return ans
        
