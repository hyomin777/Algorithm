def solution(array):
    answer = 0
    array.sort()
    flag = False
    
    max_cnt = 0
    temp_cnt = 0
    current_num = 0
    max_num = 0
    
    for num in array:
        if num != current_num:
            current_num = num
            temp_cnt = 0
        
        temp_cnt += 1
        if temp_cnt == max_cnt:
            flag = True
            
        if temp_cnt > max_cnt:
            max_cnt = temp_cnt
            max_num = num
            flag = False

    return -1 if flag else max_num