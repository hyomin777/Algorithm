class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            sorted_word = sorted(word)
            key = tuple(sorted_word)

            if not key in dict:
                dict[key] = []

            dict[key].append(word)

        return list(dict.values())