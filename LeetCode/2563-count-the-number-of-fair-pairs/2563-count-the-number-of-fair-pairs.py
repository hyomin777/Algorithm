class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n - 1):
            left = i + 1
            right = n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < lower - nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            start = left
            left = i + 1
            right = n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > upper - nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            end = right
            
            count += max(0, end - start + 1)
        
        return count
            