#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, A: "List[int]", T: "List[int]", x: "List[int]",
          y: "List[int]"):
    shifted = 0
    n = len(A)
    for t, i, j in zip(T, x, y):
        mod = shifted % n
        if t == 1:
            A[(j - 1 - mod) % n], A[(i - 1 - mod) %
                                    n] = A[(i - 1 - mod) %
                                           n], A[(j - 1 - mod) % n]
        elif t == 2:
            shifted += 1
        else:
            print(A[(i - 1 - mod) % n])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, Q, A, T, x, y)


if __name__ == '__main__':
    main()
