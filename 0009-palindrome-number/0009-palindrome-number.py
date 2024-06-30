class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        temp = ''

        for i in reversed(str_x):
            temp += i

        if x == int(temp):
            return True
        return False