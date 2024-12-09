def solution(num_list):
    even = 0
    odd = 0
    
    for i, num in enumerate(num_list):
        if i % 2 == 0:
            even += num
        else:
            odd += num
    
    return even if even >= odd else odd