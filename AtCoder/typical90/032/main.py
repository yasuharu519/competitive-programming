#!/usr/bin/env python3
import sys
from itertools import permutations


def solve(N: int, A: "List[List[int]]", M: int, X: "List[int]",
          Y: "List[int]"):
    kenaku = [[False] * N for _ in range(N)]
    for x, y in zip(X, Y):
        kenaku[x - 1][y - 1] = True
        kenaku[y - 1][x - 1] = True

    ans = float('inf')
    for pattern in permutations(range(N)):
        flag = False
        total = 0
        for i in range(len(pattern)):
            total += A[pattern[i]][i]
            if i < N - 1 and kenaku[pattern[i]][pattern[i + 1]]:
                flag = True
        if not flag:
            ans = min(ans, total)
    print(ans if ans != float('inf') else -1)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)]
         for _ in range(N)]  # type: "List[List[int]]"
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, A, M, X, Y)


if __name__ == '__main__':
    main()
