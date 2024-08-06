from typing import List

class Solution:
    def __init__(self):
        self.digit_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.output = []
    
    def backtrack(self, digits: str, index: int, path: List[str]):
        if index == len(digits):
            self.output.append("".join(path))
            return
        
        possible_letters = self.digit_to_char[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            self.backtrack(digits, index + 1, path)
            path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.output = []
        self.backtrack(digits, 0, [])
        return self.output
