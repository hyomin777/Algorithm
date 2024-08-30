class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}

        for char in jewels:
            dict[char] = 0

        for char in stones:
            if char in dict:
                dict[char] += 1

        return sum(dict.values())