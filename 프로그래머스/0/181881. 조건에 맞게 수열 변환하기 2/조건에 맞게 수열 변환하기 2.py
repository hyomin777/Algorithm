def solution(arr):
    answer = []
    cnt = 0

    for num in arr:
        if num >= 50 and num % 2 == 0:
            answer.append(num//2)
        elif num < 50 and num % 2 != 0:
            answer.append(num*2+1)
                
    while answer != arr:
        arr = answer
        answer = []
        cnt += 1
        for num in arr:
            if num >= 50 and num % 2 == 0:
                answer.append(num//2)
            elif num < 50 and num % 2 != 0:
                answer.append(num*2+1)
        
    return cnt-1