from heapq import heappush, heappop
from itertools import accumulate

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7

        prefix_sums = list(accumulate(nums, initial=0))
        min_heap = []
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_sum = prefix_sums[j] - prefix_sums[i]
                heappush(min_heap, sub_sum)
        
        result = 0
        for _ in range(left - 1):
            heappop(min_heap)
        
        for _ in range(right - left + 1):
            result += heappop(min_heap)
            result %= MOD
        
        return result

