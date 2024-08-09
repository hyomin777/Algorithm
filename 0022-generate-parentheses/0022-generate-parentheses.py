class Solution:

    def backtrack(self, n, res, formed_parentheses, left, right):
        if len(formed_parentheses) == 2 * n:
            res.append(formed_parentheses)
            return

        if left < n:
            self.backtrack(n, res, formed_parentheses + '(', left + 1, right)

        if right < left:
            self.backtrack(n, res, formed_parentheses + ')', left, right + 1)
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n, res, '', 0, 0) 
        return res