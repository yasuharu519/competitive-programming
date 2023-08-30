#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    mapA = defaultdict(int)
    mapB = defaultdict(int)
    mapC = defaultdict(int)

    for a in A:
        mapA[a % 46] += 1
    for b in B:
        mapB[b % 46] += 1
    for c in C:
        mapC[c % 46] += 1

    res = 0
    for key_a, val_a in mapA.items():
        for key_b, val_b in mapB.items():
            for key_c, val_c in mapC.items():
                if (key_a + key_b + key_c) % 46 == 0:
                    res += val_a * val_b * val_c
    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)


if __name__ == '__main__':
    main()
