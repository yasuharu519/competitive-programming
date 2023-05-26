#!/usr/bin/env python3
import sys
import math
import bisect


def eratosthenes(N: int):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False

    for i in range(2, math.ceil(math.sqrt(N) + 1)):
        if primes[i] == False:
            continue

        for j in range(i * i, N + 1, i):
            primes[j] = False

    return [i for i, prime in enumerate(primes) if prime]


def solve(N: int):
    primes = eratosthenes(N)
    count = 0

    for i in range(len(primes)):
        a = primes[i]
        squareA = a * a

        for j in range(i + 1, len(primes)):
            b = primes[j]
            squareAB = squareA * b

            maxSquareC = N // squareAB
            if maxSquareC < b * b:
                break

        idx = bisect.bisect_left(primes, maxSquareC**0.5)
        print(idx)
        if idx <= 0:
            continue
        elif idx < len(primes) and primes[idx]**2 == maxSquareC:
            count += idx - j
        else:
            count += idx - j - 1

        print(a, count)

    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
