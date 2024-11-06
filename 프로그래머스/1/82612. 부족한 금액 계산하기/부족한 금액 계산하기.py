def solution(price, money, count):
    total_money = 0
    
    for i in range(1, count+1):
        total_money += i * price
        
    answer = money - total_money
    if answer < 0:
        return -answer
    return 0