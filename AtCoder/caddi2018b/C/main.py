#!/usr/bin/env python3
from collections import defaultdict

def prime_factorize(n):
    res = defaultdict(int)
    while n % 2 == 0:
        res[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            res[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        res[n] += 1
    return res

def main():
    N, P = list(map(int, input().strip().split()))
    primes = prime_factorize(P)
    res = 1
    for k, v in primes.items():
        div = v // N
        if div:
            res *= pow(k, div)
    print(res)

if __name__ == '__main__':
    main()
