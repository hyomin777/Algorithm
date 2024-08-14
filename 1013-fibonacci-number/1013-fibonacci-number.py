class Solution:
    def fib(self, n: int) -> int:
        dp = [1] * (n+1)
        dp[0] = 0

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]