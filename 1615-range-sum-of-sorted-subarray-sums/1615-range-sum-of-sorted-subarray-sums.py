class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray = []

        for i in range(n):
            for j in range(i, n):
                sum_of_subarray = sum(nums[i:j + 1])
                subarray.append(sum_of_subarray)
        
        subarray.sort()
        result = sum(subarray[left-1:right]) % (10**9+7)
        
        return result
