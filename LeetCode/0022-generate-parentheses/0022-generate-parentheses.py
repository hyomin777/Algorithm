class Solution:


    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(parentheses, left, right):
            if len(parentheses) == (n * 2):
                res.append(parentheses)
                return

            if left < n:
                backtrack(parentheses + "(", left + 1, right)

            if right < left:
                backtrack(parentheses + ")", left, right + 1)

        backtrack("", 0, 0)

        return res
            