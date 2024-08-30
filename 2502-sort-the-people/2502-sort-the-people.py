class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict = {}
        result = []
        n = len(names)

        for i in range(n):
            dict[heights[i]] = names[i]

        sorted_heights = sorted(heights, reverse=True)
        for height in sorted_heights:
            result.append(dict[height])

        return result