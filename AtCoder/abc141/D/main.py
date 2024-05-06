#!/usr/bin/env python3
import heapq
def main():
    N, M = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))

    heap = []
    for a in A:
        heapq.heappush(heap, -a)
    
    while M > 0 and heap:
        p = -1 * heapq.heappop(heap)
        if not p:
            break
        heapq.heappush(heap, -1 * (p // 2))
        M -= 1
    
    print(sum(heap) * -1)
    return



if __name__ == '__main__':
    main()
