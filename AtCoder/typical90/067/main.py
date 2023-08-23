#!/usr/bin/env python3
import sys


def eightToTen(N: int) -> int:
    if N < 10:
        return N
    else:
        div, mod = divmod(N, 10)
        return mod + 8 * eightToTen(div)


def tenToNine(N: int) -> int:
    res = 0
    level = 0
    while N:
        div, mod = divmod(N, 9)
        res += mod * (10**level)
        N = div
        level += 1
    return res


def eightToFive(N: int) -> int:
    return int("".join(["5" if x == "8" else x for x in str(N)]))


def solve(N: int, K: int):

    for _ in range(K):
        N = eightToFive(tenToNine(eightToTen(N)))
    print(N)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    # print(tenToNine(eightToTen(21)))
    main()
