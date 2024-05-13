#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    total = A[0]
    result = 0
    for i, a in enumerate(A[1:]):
        l = len(str(a))
        past = i + 1

        result += (total * pow(10, l)) % MOD
        result += (a * past) % MOD
        result = result % MOD

        total += a
    print(result)

if __name__ == '__main__':
    main()
