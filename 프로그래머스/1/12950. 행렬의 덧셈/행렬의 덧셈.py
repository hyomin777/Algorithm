def solution(arr1, arr2):
    answer = []
    
    for row1, row2 in zip(arr1, arr2):
        sum = []
        for col1, col2 in zip(row1, row2):
            sum.append(col1+col2)
        answer.append(sum)
    
    return answer