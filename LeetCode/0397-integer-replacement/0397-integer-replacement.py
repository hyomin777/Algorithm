class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        memo[1] = 0

        def recursion(idx):
            if idx in memo:
                return memo[idx]

            if idx % 2 == 0:
                memo[idx] = recursion(idx // 2) + 1 
            else:
                memo[idx] = min(recursion(idx-1), recursion(idx+1)) + 1
            
            return memo[idx]

        return memoization(n)

