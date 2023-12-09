#!/usr/bin/env python3
import sys


def solve(N: int, C: int, K: int, T: "List[int]"):

    T.sort()

    earliest = T[0]
    bus_count = 1
    acc = 1

    for t in T[1:]:
        if t > earliest + K:
            bus_count += 1
            acc = 1
            earliest = t
        else:
            if acc >= C:
                bus_count += 1
                acc = 1
                earliest = t
            else:
                acc += 1
    print(bus_count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C, K, T)

if __name__ == '__main__':
    main()
