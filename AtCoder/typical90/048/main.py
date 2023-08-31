#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    problems = B[:]
    problems.extend([a - b for a, b in zip(A, B)])
    problems.sort(reverse=True)
    print(sum(problems[:K]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, K, A, B)


if __name__ == '__main__':
    main()
