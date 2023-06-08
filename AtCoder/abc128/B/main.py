#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(N: int, S: "List[str]", P: "List[int]"):
    d = defaultdict(list)
    for i, (city, point) in enumerate(zip(S, P)):
        d[city].append((point, i))
    
    for _, value in sorted(d.items(), key= lambda x: x[0]):
        for v in sorted(value, key=lambda x: x[0],  reverse=True):
            print(v[1]+1)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        P[i] = int(next(tokens))
    solve(N, S, P)

if __name__ == '__main__':
    main()
