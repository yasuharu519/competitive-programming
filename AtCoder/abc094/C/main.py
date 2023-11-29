#!/usr/bin/env python3
import sys

from collections import Counter

def solve(N: int, X: "List[int]"):
    sorted_list = sorted(X)
    a, b = sorted_list[N // 2 - 1], sorted_list[N // 2]

    id_map = {}
    for i, v in enumerate(sorted_list):
        if v in id_map:
            continue
        id_map[v] = i

    for x in X:
        i = id_map[x]
        if i < N // 2:
            print(b)
        else:
            print(a)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()
