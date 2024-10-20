class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        dp = [10000] * (n)
        dp[0] = 0

        for i in range(n):
            jump = nums[i]
            last = min(n, i + jump + 1)

            for j in range(i+1, last):
                dp[j] = min(dp[i] + 1, dp[j])

        return dp[n-1]