def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    longer = max(rows, cols)
    answer = [[0] * longer for _ in range(longer)]
    
    for row in range(rows):
        for col in range(cols):
            answer[row][col] = arr[row][col]
            
    return answer