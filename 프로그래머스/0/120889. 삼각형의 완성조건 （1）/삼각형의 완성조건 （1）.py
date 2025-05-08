def solution(sides):
    logest_side = max(sides)
    two_side_sum = sum(sides) - logest_side
    
    if logest_side < two_side_sum:
        return 1
    return 2