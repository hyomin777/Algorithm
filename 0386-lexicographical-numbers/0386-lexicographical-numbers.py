class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []

        for i in range(1, n+1):
            arr.append(str(i))

        arr.sort()

        result = []
        for i in arr:    
            result.append(int(i))

        return result