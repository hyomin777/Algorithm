def solution(num_list):
    sum_square = 0
    multiply = 1
    
    for num in num_list:
        sum_square += num
        multiply *= num
    
    sum_square **= 2
    
    return 1 if sum_square > multiply else 0