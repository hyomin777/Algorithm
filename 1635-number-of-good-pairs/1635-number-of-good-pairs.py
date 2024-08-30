class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}

        for i in range(len(nums)):
            dict[i] = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    dict[i] += 1
        
        return sum(dict.values())