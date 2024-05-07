#!/usr/bin/env python3
import heapq

def main():
    N, M = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    heap = []
    for a in A:
        heapq.heappush(heap, a)
    
    result = 0
    pairs = []
    for _ in range(M):
        B, C = list(map(int, input().strip().split()))
        pairs.append((C, B))
    pairs.sort(reverse=True)

    for C, B in pairs:
        rest = B
        while rest > 0 and heap and heap[0] < C:
            result += C
            heapq.heappop(heap)
            rest -= 1
    
    print(result + sum(heap))
    return

if __name__ == '__main__':
    main()
