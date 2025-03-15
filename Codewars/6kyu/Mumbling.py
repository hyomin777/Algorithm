def accum(st):
    output = []
    cnt = 0
    for char in st:
        output.append(char.upper() + (char.lower() * cnt))
        cnt += 1
    return '-'.join(output)