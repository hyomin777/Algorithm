from itertools import permutations

def solution(k, dungeons):
    all_dungeons = list(permutations(dungeons, len(dungeons)))
    possible = []
    i = 0
    
    while i < len(all_dungeons):
        stamina = k
        count = 0
        
        for dungeon in all_dungeons[i]:
            if stamina < dungeon[0]:
                break
            
            if stamina >= dungeon[0]:
                stamina = stamina - dungeon[1]
                count += 1
                
        possible.append(count)
        i += 1        

    answer = max(possible)      
    return answer