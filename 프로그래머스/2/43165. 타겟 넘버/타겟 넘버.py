def solution(numbers, target):
    def recursion(num, cnt):
        if cnt == len(numbers):
            # 목표 숫자를 달성한 경우 1을 반환
            if num == target:
                return 1
            else:
                return 0
        
        return recursion(num + numbers[cnt], cnt + 1) + recursion(num - numbers[cnt], cnt + 1)

    return recursion(0, 0)
