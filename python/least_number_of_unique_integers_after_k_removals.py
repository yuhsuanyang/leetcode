class Solution:
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        if k == 0:
            return len(counter)
        for i in counter:
            self.heap.append(i)
            j = len(self.heap) - 1
            while j and (counter[self.heap[j]] < counter[self.heap[(j - 1) // 2]]):
                self.swap(j, (j - 1) // 2)
                j = (j - 1) // 2

        while k > 0:
            k -= counter[self.heap[0]]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            j = 0
            while j * 2 + 2 < len(self.heap):
                if counter[self.heap[j * 2 + 1]] < counter[self.heap[j * 2 + 2]]:
                    child = j * 2 + 1
                else:
                    child = j * 2 + 2
                if counter[self.heap[j]] > counter[self.heap[child]]:
                    self.swap(j, child)
                    j = child
                else:
                    break
            if len(self.heap) == 2:
                if counter[self.heap[0]] > counter[self.heap[1]]:
                    self.swap(0, 1)
        return len(self.heap) + 1 if k < 0 else len(self.heap)


            
