def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = 1000001
        
        for i, num in enumerate(arr):
            if s <= i <= e and num > k and temp > num:
                temp = num
        
        if temp != 1000001:
            answer.append(temp)
        else:
            answer.append(-1)
    
    return answer