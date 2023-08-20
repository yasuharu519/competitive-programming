#!/usr/bin/env python3
import sys
import bisect


def solve(N: int, A: "List[int]", Q: int, B: "List[int]"):
    A.sort()
    for b in B:
        i = bisect.bisect_left(A, b)
        score = float('inf')
        if i < N:
            score = min(score, abs(b-A[i]))
        if i > 0:
            score = min(score, abs(b-A[i-1]))
        print(score)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, A, Q, B)

if __name__ == '__main__':
    main()
