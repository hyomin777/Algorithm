def solution(arr, flags):
    answer = []
    
    for num, flag in zip(arr, flags):
        if flag:
            for _ in range(num*2):
                answer.append(num)
        else:
            for _ in range(num):
                answer.pop()
    return answer