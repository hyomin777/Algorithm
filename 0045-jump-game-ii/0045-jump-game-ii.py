class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n 
        dp[0] = 0 

        for i in range(n):
            max_jump = min(i + nums[i], n - 1)  # nums[i]만큼 점프, 끝 인덱스 초과 방지
            for j in range(i + 1, max_jump + 1):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
