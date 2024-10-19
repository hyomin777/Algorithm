class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        def reverse(x):
            return x[::-1]
        
        def invert(x):
            result = ''
            for char in x:
                if char == '0':
                    char = '1'
                else:
                    char = '0'
                result += char
            return result

        s = {1:'0'}
        for i in range(2, n+1):
            s[i] = s[i-1] + "1" + reverse(invert(s[i-1]))

        return s[n][k-1]