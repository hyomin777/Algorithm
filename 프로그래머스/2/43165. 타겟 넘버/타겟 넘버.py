def solution(numbers, target):
    def recursion(num, cnt):
        if cnt == len(numbers):
            if num == target:
                return 1
            else:
                return 0
        
        return recursion(num + numbers[cnt], cnt + 1) + recursion(num - numbers[cnt], cnt + 1)

    return recursion(0, 0)
