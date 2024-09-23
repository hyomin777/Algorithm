class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(n):
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)

            for word in word_set:
                length = len(word)
                if i + length <= n and s[i:i + length] == word:
                    dp[i + length] = min(dp[i + length], dp[i])
        
        return dp[n]