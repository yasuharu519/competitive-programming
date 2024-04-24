#!/usr/bin/env python3
import heapq
def main():
    N, K = list(map(int, input().strip().split()))
    heap = []
    for _ in range(N):
        a, b = list(map(int, input().strip().split()))
        heapq.heappush(heap, (a, b))
    
    while heap and K >= 0:
        a, b = heapq.heappop(heap)
        K -= b
        if K <= 0:
            print(a)
            return
    print(a)
    return

if __name__ == '__main__':
    main()
