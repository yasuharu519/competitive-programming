#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int

def main():
    A, B, C, D, E, F = list(map(int, input().strip().split()))
    left = A % MOD
    left = (left * B) % MOD
    left = (left * C) % MOD
    right = D % MOD
    right = (right * E) % MOD
    right = (right * F) % MOD
    print((left - right) % MOD)

if __name__ == '__main__':
    main()
