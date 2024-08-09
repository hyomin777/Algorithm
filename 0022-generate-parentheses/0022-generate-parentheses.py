class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(formed_parentheses, left, right):
            if len(formed_parentheses) == 2 * n:
                res.append(formed_parentheses)
                return

            if left < n:
                backtrack(formed_parentheses + '(', left + 1, right)

            if right < left:
                backtrack(formed_parentheses + ')', left, right + 1)
        
        backtrack('', 0, 0)
        return res