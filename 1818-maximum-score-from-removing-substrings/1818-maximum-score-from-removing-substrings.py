class Solution:
    def remove_ab_and_count(self, s: str, target: str, points: int):
        stack = []
        count = 0

        for char in s:
            if stack and stack[-1] + char == target:
                stack.pop()
                count += points
            else:
                stack.append(char)
        return ''.join(stack), count

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y:
            s, score1 = self.remove_ab_and_count(s, "ab", x)
            s, score2 = self.remove_ab_and_count(s, "ba", y)
        else:
            s, score1 = self.remove_ab_and_count(s, "ba", y)
            s, score2 = self.remove_ab_and_count(s, "ab", x)
    
        return score1 + score2