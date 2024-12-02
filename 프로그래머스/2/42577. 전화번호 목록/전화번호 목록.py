def solution(phone_book):
    dict = {number: True for number in phone_book}
    
    for number in phone_book:
        temp = ''
        
        for char in number[:-1]:
            temp += char
            
            if temp in dict:
                return False
            
    return True
        