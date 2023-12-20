#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: int):
    result = [S] * K + [1 if S == 10 ** 9 else S + 1] * (N - K)
    print(" ".join([str(x) for x in result]))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(N, K, S)

if __name__ == '__main__':
    main()
