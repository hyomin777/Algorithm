from bisect import bisect_left, bisect_right

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            start = bisect_left(nums, lower - nums[i], i + 1, n)
            end = bisect_right(nums, upper - nums[i], i + 1, n)
            count += (end - start)

        return count

            