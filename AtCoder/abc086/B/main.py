#!/usr/bin/env python3
import sys
import math

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(a: int, b: int):
    lenB = len(str(b))
    num = a * pow(10, lenB) + b

    c = int(math.sqrt(num))
    if c * c == num:
        print(YES)
    else:
        print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(a, b)

if __name__ == '__main__':
    main()
