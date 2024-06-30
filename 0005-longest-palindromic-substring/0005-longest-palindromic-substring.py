class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''

        for i in range(len(s)):
            temp = s[i:]
            
            while temp:
                reverse_temp = temp[::-1]
                if temp == reverse_temp and len(temp) > len(output):
                    output = temp
                
                temp = temp[:-1]

        return output