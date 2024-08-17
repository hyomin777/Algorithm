class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cnt = 0
        repeated_word = word

        while repeated_word in sequence:
            cnt += 1
            repeated_word += word

        return cnt


