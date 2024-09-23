class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(n):
            dp[i+1] = min(dp[i+1], dp[i]+1)

            for word in dictionary:
                length = len(word)

                if i+length <= n and s[i:i+length] == word:
                    dp[i+length] = min(dp[i], dp[i+length])
        
        return dp[n]
