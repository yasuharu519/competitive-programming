#!/usr/bin/env python3
import sys


def isPrime(x: int):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        i = 2
        while i*i <= x:
            if x % i == 0:
                return False
            i += 1
        return True


def solve(X: int):
    while isPrime(X) == False:
        X += 1
    print(X)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
