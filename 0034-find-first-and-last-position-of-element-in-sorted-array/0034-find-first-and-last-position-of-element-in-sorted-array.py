class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first_target_index(nums, target):
            output = -1

            for i in range(len(nums)):
                if nums[i] == target:
                    output = i
                    break

            return output

        def find_last_target_index(nums, target):
            output = 0

            for i in range(len(nums)):
                if nums[i] == target:
                    output = i

            return output

        first_idx = find_first_target_index(nums, target)

        if not first_idx == -1:
            last_idx = find_last_target_index(nums, target)
        
        else:
            last_idx = -1
        
        return [first_idx, last_idx]
            

        