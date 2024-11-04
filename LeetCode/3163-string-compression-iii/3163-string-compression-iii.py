class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return f"1{word}"
        
        result = ''
        cnt = 1

        for i in range(1, len(word)):
            prev_char = word[i-1]
            current_char = word[i]
            
            if current_char == prev_char:
                if cnt >= 9:
                    result += f"{cnt}{prev_char}"
                    cnt = 1
                else:
                    cnt += 1
            else:
                result += f"{cnt}{prev_char}"
                cnt = 1
            
        result += f"{cnt}{word[-1]}"
            
            
        return result