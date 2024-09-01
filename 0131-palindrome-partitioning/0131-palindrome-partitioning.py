class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start: int, current: List[str]):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]

                if substring == substring[::-1]:
                    current.append(substring)
                    backtrack(end+1, current)
                    current.pop()
        
        backtrack(0, [])

        return result
