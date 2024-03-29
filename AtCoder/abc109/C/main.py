#!/usr/bin/env python3
import sys
import math


def solve(N: int, X: int, x: "List[int]"):
    print(math.gcd(*[abs(xi-X) for xi in x]))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, x)

if __name__ == '__main__':
    main()
