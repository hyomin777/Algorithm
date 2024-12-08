def solution(arr):
    n = len(arr)
    
    start_pointer = 0
    end_pointer = n - 1
    
    start_idx = -1
    end_idx = -1
    
    while start_pointer <= end_pointer:
        if start_idx != -1 and end_idx != -1:
            break
        
        if arr[start_pointer] != 2:
            start_pointer += 1
        else:
            start_idx = start_pointer
        
        if arr[end_pointer] != 2:
            end_pointer -= 1
        else:
            end_idx = end_pointer
        
    if start_idx == -1 and end_idx == -1:
        return [-1]
    
    if start_idx == -1 or end_idx == -1:
        return [2]
    
    return arr[start_idx:end_idx+1]
