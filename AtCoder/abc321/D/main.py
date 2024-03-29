#!/usr/bin/env python3
import sys


def solve(N: int, M: int, P: int, A: "List[int]", B: "List[int]"):
    A.sort()
    B.sort()

    rest = 0
    total = 0
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a + b < P:
                total += (a + b)
            else:
                rest += (M - j)
                break
    print(total + rest * P)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, P, A, B)


if __name__ == '__main__':
    main()
