#!/usr/bin/env python3
import sys


def solve(K: int, N: int, A: "List[int]"):
    A.append(A[0]+K)

    diff = 0
    for i in range(N):
        diff = max(diff, A[i+1]-A[i])
    print(K-diff)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(K, N, A)

if __name__ == '__main__':
    main()
