def solution(box, n):
    width, length, height = box
    
    width_max = width // n
    length_max = length // n
    height_max = height // n
    
    return width_max*length_max*height_max