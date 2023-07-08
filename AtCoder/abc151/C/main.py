#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(N: int, M: int, p: "List[int]", S: "List[str]"):
    accepted = defaultdict(int)
    penalty = defaultdict(int)

    for i, result in zip(p, S):
        if result == "AC":
            accepted[i] += 1
        elif accepted[i] == 0:
            penalty[i] += 1

    resultAccept = sum(1 for v in accepted.values() if v > 0)
    resultReject = sum(penalty[i] for i in accepted.keys() if accepted[i] > 0)

    print(f"{resultAccept} {resultReject}")
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int()] * (M)  # type: "List[int]"
    S = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        p[i] = int(next(tokens))
        S[i] = next(tokens)
    solve(N, M, p, S)

if __name__ == '__main__':
    main()
