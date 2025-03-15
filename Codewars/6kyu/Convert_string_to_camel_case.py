def to_camel_case(text):
    output = ''
    flag = False
    
    for char in text:
        if char == "-" or char == "_":
            flag = True
        else:
            if flag:
                output += char.upper()
            else:
                output += char
            flag = False
            
    return output