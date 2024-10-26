class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []

        for i in range(len(triangle)):
            dp.append([])
            for j in range(len(triangle[i])):
                dp[i].append(triangle[i][j])

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])-1):
                dp[i][j] += min(dp[i-1][j-1], dp[i-1][j])       

            dp[i][0] += dp[i-1][0]
            dp[i][-1] += dp[i-1][-1]


        return min(dp[-1])