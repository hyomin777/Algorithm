str = input()

new_str = ''
for char in str:
    if char.upper() == char:
        new_str += char.lower()
    else:
        new_str += char.upper()
        
print(new_str)