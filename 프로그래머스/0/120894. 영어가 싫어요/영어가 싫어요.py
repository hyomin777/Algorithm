dictionary = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def solution(numbers):
    answer = ''
    temp = ''
    
    for char in numbers:
        temp += char
        if temp in dictionary:
            answer += str(dictionary[temp])
            temp = ''
    
    return int(answer)