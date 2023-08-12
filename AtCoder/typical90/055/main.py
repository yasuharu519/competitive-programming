#!/usr/bin/env python3
import sys
from itertools import combinations
from functools import reduce


def solve(N: int, P: int, Q: int, A: "List[int]"):
    counter = 0
    for a, b, c, d, e in combinations(A, 5):
        if a % P * b % P * c % P * d % P * e % P == Q:
            counter += 1
    print(counter)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q, A)


if __name__ == '__main__':
    main()
