import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_map = {}

    for calc in operations:
        if calc.startswith("I"):
            num = int(calc.split()[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_map[num] = entry_map.get(num, 0) + 1
        elif entry_map:
            if calc == "D 1":
                while max_heap and entry_map.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_map[max_val] -= 1
                    if entry_map[max_val] == 0:
                        del entry_map[max_val]
            elif calc == "D -1":
                while min_heap and entry_map.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_map[min_val] -= 1
                    if entry_map[min_val] == 0:
                        del entry_map[min_val]

    if not entry_map:
        return [0, 0]
    
    while min_heap and entry_map.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_map.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    max_val = -max_heap[0]
    min_val = min_heap[0]
    
    return [max_val, min_val]
