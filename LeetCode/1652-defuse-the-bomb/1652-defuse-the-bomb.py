class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        n = len(code)
        
        for i in range(n):
            if k > 0:
                temp = 0
                for j in range(1, k+1):
                    temp += code[(i+j) % n]
                result.append(temp)
                
            if k < 0:
                temp = 0
                for j in range(-1, k-1, -1):
                    temp += code[(i+j) % n]
                result.append(temp)
            
            if k == 0:
                result.append(0)
                
        return result
                