#!/usr/bin/env python3
import sys
import math

def gcd(a: int, b: int) -> int:
    if b > a:
        a, b = b, a
    
    while a % b != 0:
        _, mod = divmod(a, b)
        a, b = b, mod
    return b


def solve(N: int, A: "List[int]"):
    answer = A[0]

    for a in A[1:]:
        answer = gcd(a, answer)

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
