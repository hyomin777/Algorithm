def solution(operations):
    answer = []
    
    for calc in operations:
        if calc.startswith("I"):
            answer.append(int(calc[1:]))
        elif not answer:
            continue
        elif calc == "D 1":
            answer.remove(max(answer))
        elif calc == "D -1":
            answer.remove(min(answer))
            
    if not answer:
        return [0, 0]
    return [max(answer), min(answer)]