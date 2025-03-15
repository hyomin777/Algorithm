def duplicate_count(text):
    cnt = 0
    exist = set()
    duplicated = set()
    
    for char in text:
        char = char.lower()
        
        if char not in exist:
            exist.add(char)
        else:
            if char not in duplicated:
                duplicated.add(char)
                cnt +=1

    return cnt