from itertools import permutations

def solution(k, dungeons):
    all_dungeons = list(permutations(dungeons,len(dungeons)))
    possible = []
    i = 0
    
    while i < len(all_dungeons):
        stamina = k
        count = 0
        
        for j in all_dungeons[i]:
            
            if stamina >= j[0]:
                stamina = stamina - j[1]
                count += 1
                
            elif stamina < j[0]:
                break

        possible.append(count)
        i += 1        

    answer = max(possible)      
    return answer