class Solution:
    def integerReplacement(self, n: int) -> int:
        memo  = {}

        def memoization(idx):
            if idx == 1:
                return 0

            if idx in memo:
                return memo[idx]

            if idx % 2 == 0:
                memo[idx] = memoization(idx // 2) + 1 
            else:
                memo[idx] = min(memoization(idx-1), memoization(idx+1)) + 1
            
            return memo[idx]

        return memoization(n)

