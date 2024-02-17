#no. 1642
class Solution:
    def __init__(self):
        self.heap = []

    def heap_swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def heap_push(self, num):
        self.heap.append(num)
        k = len(self.heap) - 1
        while k and self.heap[k] < self.heap[(k - 1) // 2]:
            self.heap_swap(k, (k - 1) // 2)
            k = (k - 1) // 2
    
    def heap_pop(self):
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        k = 0
        while k * 2 + 2 < len(self.heap):
            if self.heap[k * 2 + 2] < self.heap[k * 2 + 1]:
                child = k * 2 + 2
            else:
                child = k * 2 + 1
            if self.heap[k] > self.heap[child]:
                self.heap_swap(k, child)
                k = child
            else:
                break
        if len(self.heap) == 2:
            if self.heap[0] > self.heap[1]:
                self.heap_swap(0, 1)
            return val
        return val

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                diff = heights[i] - heights[i - 1]
                self.heap_push(diff)
            if len(self.heap) > ladders:
                bricks -= self.heap_pop()
            if bricks < 0:
                return i - 1
        return len(heights) - 1
                    



