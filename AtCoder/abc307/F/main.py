#!/usr/bin/env python3
import sys


def solve(N: int, M: int, U: "List[int]", V: "List[int]", W: "List[int]", K: int, A: "List[int]", D: int, X: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    W = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
        W[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    D = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(D)]  # type: "List[int]"
    solve(N, M, U, V, W, K, A, D, X)

if __name__ == '__main__':
    main()
