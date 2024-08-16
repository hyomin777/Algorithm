class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = [char for char in s]
        
        while queue:
            char = queue.pop(0)

            if not char in t:
                return False
            
            for i in range(len(t)):
                if t[i] == char:
                    t = t[i+1:]
                    break

        return True
