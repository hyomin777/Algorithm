class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start: int, path: List[str], result: List[List[str]]):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end, path, result)
                    path.pop()
        
        backtrack(0, [], result)

        return result
