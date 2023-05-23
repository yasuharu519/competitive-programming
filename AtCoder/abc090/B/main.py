#!/usr/bin/env python3
import sys


def isPalindrome(num: int):
    s = str(num)
    return s == s[::-1]

def solve(A: int, B: int):
    count = sum([1 for x in range(A, B+1) if isPalindrome(x)])
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
