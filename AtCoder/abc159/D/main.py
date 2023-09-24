#!/usr/bin/env python3
import sys
import math
from collections import Counter


def solve(N: int, A: "List[int]"):
    c = Counter(A)
    base = {}
    total = 0
    # base count
    for key, val in c.items():
        res = 0
        if val > 1:
            res = math.comb(val, 2)
        base[key] = res
        total += res

    for a in A:
        num_in_base = base[a]
        if num_in_base == 0:
            print(total)
        elif num_in_base == 1:
            print(total - 1)
        else:
            calc = math.comb(c[a] - 1, 2)
            diff = calc - num_in_base
            print(total + diff)

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
