def filter_list(l):
    filtered_list = []
    for element in l:
        if type(element) is int:
            filtered_list.append(element)

    return filtered_list