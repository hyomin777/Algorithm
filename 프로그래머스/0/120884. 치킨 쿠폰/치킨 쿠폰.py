def solution(chicken):
    answer = 0
    left_coupon = 0
    
    while chicken >= 10:
        able_chicken = chicken // 10
        left_coupon = chicken % 10
        answer += able_chicken
        
        chicken = able_chicken + left_coupon
        
    return answer