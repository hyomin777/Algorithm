def op(num):
    cnt = 0
    while num > 1:
        if num%2 == 0:
            num = num//2
        else:
            num = (num-1)//2
        cnt += 1
    return cnt
    
def solution(num_list):
    answer = 0
    for num in num_list:
        answer += op(num)
    return answer