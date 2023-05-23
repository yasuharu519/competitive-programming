#!/usr/bin/env python3
import sys


def solve(N: int, H: "List[int]"):
    current = H[0]
    countMax = 0
    countCurrent = 0
    for i in H[1:]:
        if i <= current:
            countCurrent += 1
            countMax = max(countMax, countCurrent)
        else:
            countCurrent = 0
        current = i
    print(countMax)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)

if __name__ == '__main__':
    main()
