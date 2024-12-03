def solution(genres, plays):
    answer = []
    total_play = {}
    idx = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if not genre in total_play:
            total_play[genre] = play
            idx[genre] = [[play, i]]
            
        else:
            total_play[genre] += play
            idx[genre].append([play, i])

    for genre in idx:
        idx[genre].sort(key = lambda x: x[0], reverse=True)

    total_play = sorted(
        total_play.items(),
        key = lambda x: x[1],
        reverse=True
    )
    
    for genre, _ in total_play:
        answer.extend([index for _, index in idx[genre][:2]])
        
    return answer
    