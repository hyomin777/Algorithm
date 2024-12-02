def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)

    for priority in emergency:
        answer.append(sorted_emergency.index(priority)+1)
    
    return answer
