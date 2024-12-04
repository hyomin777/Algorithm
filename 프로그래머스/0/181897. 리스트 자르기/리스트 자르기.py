def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    
    if n == 1:
        for num in num_list[:b+1]:
            answer.append(num)
            
    if n == 2:
        for num in num_list[a:]:
            answer.append(num)
    
    if n == 3:
        for num in num_list[a:b+1]:
            answer.append(num)
    
    if n == 4:
        for num in num_list[a:b+1:c]:
            answer.append(num)
    
    return answer