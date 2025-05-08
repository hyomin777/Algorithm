def solution(s1, s2):
    answer = 0
    for str1 in s1:
        for str2 in s2:
            if str1 == str2:
                answer += 1
            
    return answer