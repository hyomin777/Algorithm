class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            dict[i] = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] > nums[j]:
                        dict[i] += 1

        return dict.values()