class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''

        for digit in digits:
            num += str(digit)

        num = int(num) + 1

        array = []

        for i in str(num):
            array.append(int(i))

        return array



        
        