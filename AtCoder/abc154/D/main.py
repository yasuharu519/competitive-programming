#!/usr/bin/env python3
import sys


def solve(N: int, K: int, p: "List[int]"):
    prefix = []
    for pi in p:
        r = ((1 + pi) * pi) / 2 / pi
        prefix.append(r)

    currentSum = sum(prefix[:K])
    res = currentSum
    for i in range(1, N - K + 1):
        currentSum -= prefix[i - 1]
        currentSum += prefix[i + K - 1]
        res = max(res, currentSum)

    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, p)


if __name__ == '__main__':
    main()
