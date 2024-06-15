#!/usr/bin/env python3
import math

YES = "POSSIBLE"
NO = "IMPOSSIBLE"


def main():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    maxA = max(A)

    g = math.gcd(*A)
    print(YES if K % g == 0 and K <= maxA else NO)

if __name__ == '__main__':
    main()
