#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict


def solve(N: int, S: str):
    counter = Counter(S)

    res = 0
    tmp = defaultdict(int)

    for i in S[:-1]:
        tmp[i] += 1
        counter[i] -= 1
        if counter[i] == 0:
            del counter[i]

        # count
        c = 0
        for key in tmp.keys():
            if key in counter:
                c += 1
        res = max(res, c)

    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()
