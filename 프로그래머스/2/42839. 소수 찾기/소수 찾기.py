from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
        

def solution(numbers):
    answer = 0
    able_numbers = set()
    
    for length in range(1, len(numbers)+1):
        for permutation in permutations(numbers, length):
            able_numbers.add(int(''.join(permutation)))
                              
    print(able_numbers)
    for number in able_numbers:
        if is_prime(number):
            answer += 1

    return answer