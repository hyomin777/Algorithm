class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        length = len(s)

        for i in range(length+1):
            for j in range(i, length+1):
                word = s[i:j]
                if word == word[::-1] and len(word) > len(result):
                    result = word
        
        return result
