def solution(str_list):
    for idx, char in enumerate(str_list):
        if char == "l":
            return str_list[:idx]
        
        if char == "r":
            return str_list[idx+1:]
        
    return []