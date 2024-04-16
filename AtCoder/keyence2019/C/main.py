#!/usr/bin/env python3
from typing import List
import heapq

def solve(N: int, A: List[int], B: List[int]):

    passed = []
    not_passed = []
    total_a = 0
    total_b = 0

    for a, b in zip(A, B):
        total_a += a
        total_b += b
        if a > b:
            heapq.heappush(passed, -1 * (a-b))
        elif a < b:
            heapq.heappush(not_passed, b-a)
    
    if total_b > total_a:
        print(-1)
        return
    
    count = 0
    diff = 0
    while not_passed and passed:
        diff += -1 * heapq.heappop(passed)
        count += 1

        while diff and not_passed and diff >= not_passed[0]:
            t = heapq.heappop(not_passed)
            count += 1
            diff -= t

    print(count)
    return


def main():
    N = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    solve(N, A, B)

if __name__ == '__main__':
    main()
