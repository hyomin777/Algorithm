class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        prev_value = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for char in reversed(s):
            value = roman[char]
            if value < prev_value:
                output -= value
            else:
                output += value
            prev_value = value

        return output