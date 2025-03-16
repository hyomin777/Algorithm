import sys

input = sys.stdin.readline
N = int(input())

class MaxHeap():
    def __init__(self):
        self.heap = [None]

    def push(self, x):
        self.heap.append(x)

        idx = len(self.heap)-1
        while idx > 1 and self.heap[idx//2] < x:
            self.heap[idx], self.heap[idx //
                                      2] = self.heap[idx//2], self.heap[idx]
            idx = idx // 2

    def pop(self):
        if len(self.heap) <= 1:
            return 0

        x = self.heap[1]
        if len(self.heap) <= 2:
            self.heap.pop()
            return x

        self.heap[1] = self.heap.pop()
        self._heapify()
        return x

    def _heapify(self):
        idx = 1
        n = len(self.heap)
        while True:
            left_child = idx*2
            right_child = idx*2+1

            if right_child < n and self.heap[right_child] > self.heap[idx]:
                if self.heap[left_child] > self.heap[right_child]:
                    self.heap[idx], self.heap[left_child] = self.heap[left_child], self.heap[idx]
                    idx = idx*2
                else:
                    self.heap[idx], self.heap[right_child] = self.heap[right_child], self.heap[idx]
                    idx = idx*2+1

            elif left_child < n and self.heap[left_child] > self.heap[idx]:
                self.heap[idx], self.heap[left_child] = self.heap[left_child], self.heap[idx]
                idx = idx*2

            else:
                break


heap = MaxHeap()

for _ in range(N):
    n = int(input())

    if n == 0:
        print(heap.pop())
    else:
        heap.push(n)

