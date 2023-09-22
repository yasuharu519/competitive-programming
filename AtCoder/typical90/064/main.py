#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, A: "List[int]", L: "List[int]", R: "List[int]",
          V: "List[int]"):
    n = len(A)
    prefix = [0]
    for i in range(1, n):
        prefix.append(A[i] - A[i - 1])
    # [0, 1, 1]

    base = sum([abs(x) for x in prefix])

    for l, r, v in zip(L, R, V):
        l, r = l - 1, r - 1

        if l > 0:
            base -= abs(prefix[l])
            prefix[l] += v
            base += abs(prefix[l])
        if r < n - 1:
            base -= abs(prefix[r + 1])
            prefix[r + 1] -= v
            base += abs(prefix[r + 1])
        print(base)
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
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    V = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, Q, A, L, R, V)


if __name__ == '__main__':
    main()
