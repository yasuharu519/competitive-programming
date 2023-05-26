#!/usr/bin/env python3
import sys
from itertools import permutations


def solve(N: int, P: "List[int]", Q: "List[int]"):
    permutation = list(permutations(range(1, N + 1)))
    pIndex = permutation.index(tuple(P))
    qIndex = permutation.index(tuple(Q))

    print(abs(pIndex - qIndex))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)


if __name__ == '__main__':
    main()
