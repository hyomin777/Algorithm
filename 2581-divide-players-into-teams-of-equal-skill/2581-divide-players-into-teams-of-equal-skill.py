class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sorted_skill = sorted(skill)
        result = 0
        temp = sorted_skill[0] + sorted_skill[-1]
        for i in range(len(skill) // 2):

            if temp != sorted_skill[i] + sorted_skill[-i-1]:
                return -1

            result += sorted_skill[i] * sorted_skill[-i-1]

        return result