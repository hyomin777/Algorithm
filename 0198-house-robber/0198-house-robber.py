class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

                
        dp = [0] * n
        dp[0] = nums[0]
        if n < 2:
            return dp[0]

        dp[1] = nums[1]
        if n < 3:
            return max(nums)

        dp[2] = nums[2] + dp[0]
        if n < 4:
            return max(dp)

        dp[3] = max(dp[0] + nums[3], dp[1] + nums[3])

        for i in range(3, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i])

        return max(dp)