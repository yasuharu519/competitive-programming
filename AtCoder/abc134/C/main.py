#!/usr/bin/env python3
import sys
from collections import Counter

def solve(N: int, A: "List[int]"):
    lht = []
    current = float('-inf')
    for a in A:
        current = max(current, a)
        lht.append(current)
    
    current = float('-inf')
    rht = [0] * N
    for i in range(N-1, -1, -1):
        num = A[i]
        current = max(current, num)
        rht[i] = current
    
    for i in range(N):
        ans = float('-inf')
        if (0 < i):
            ans = max(ans, lht[i-1])
        if (i < N-1):
            ans = max(ans, rht[i+1])
        print(ans)
    return




def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
