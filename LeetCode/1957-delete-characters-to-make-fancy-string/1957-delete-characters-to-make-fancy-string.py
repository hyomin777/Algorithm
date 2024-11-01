class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        result = s[0]
        length = 1
        
        prev_char = ''
        for i in range(1, len(s)):
            prev_char = s[i-1] 
            char = s[i]
            if char == prev_char:
                length += 1
                
                if length >= 3:
                    continue
                else:
                    result += char
                    
            else:
                length = 1
                result += char
                
        return result
                    