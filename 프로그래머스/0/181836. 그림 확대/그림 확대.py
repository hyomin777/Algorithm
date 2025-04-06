def solution(picture, k):
    answer = []
    
    for pixels in picture:
        for i in range(k):
            expanded_pixels = ''
            for pixel in pixels :
                expanded_pixels += pixel * k
            answer.append(expanded_pixels)
            
    return answer