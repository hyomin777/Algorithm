class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dict = {}
    
        rank = 1
        sorted_arr_set = sorted(set(arr))

        for num in sorted_arr_set:
            dict[num] = rank
            rank += 1

        result = []

        for num in arr:
            result.append(dict[num])

        return result