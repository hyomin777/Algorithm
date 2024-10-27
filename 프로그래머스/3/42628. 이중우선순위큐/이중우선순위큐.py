import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_map = set()

    for calc in operations:
        if calc.startswith("I"):
            num = int(calc.split()[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_map.add(num)
        elif entry_map:
            if calc == "D 1":
                while max_heap and -max_heap[0] not in entry_map:
                    heapq.heappop(max_heap)
                if max_heap:
                    entry_map.remove(-heapq.heappop(max_heap))
            elif calc == "D -1":
                while min_heap and min_heap[0] not in entry_map:
                    heapq.heappop(min_heap)
                if min_heap:
                    entry_map.remove(heapq.heappop(min_heap))

    while min_heap and min_heap[0] not in entry_map:
        heapq.heappop(min_heap)
    while max_heap and -max_heap[0] not in entry_map:
        heapq.heappop(max_heap)

    if not entry_map:
        return [0, 0]
    
    max_val = -max_heap[0]
    min_val = min_heap[0]
    
    return [max_val, min_val]
