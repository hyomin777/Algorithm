def solution(ranks, attendances):
    top_three = [(101, 101), (101, 101), (101, 101)]

    for idx, value in enumerate(zip(ranks, attendances)):
        rank, attendance = value
        if not attendance:
            continue
        if rank < max(top_three)[0]:
            top_three.remove(max(top_three))
            top_three.append((rank, idx))
    
    top_three.sort()
    return top_three[0][1] * 10000 + top_three[1][1] * 100 + top_three[2][1]