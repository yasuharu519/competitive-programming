#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    answer = 0
    numOdd, numEven = 0, 0
    for v in [A, B, C]:
        if v % 2 == 0:
            numEven += 1
        else:
            numOdd += 1

    if numOdd == 2:
        answer += 1
        if A % 2 == 1:
            A += 1
        if B % 2 == 1:
            B += 1
        if C % 2 == 1:
            C += 1
    elif numEven == 2:
        answer += 1
        if A % 2 == 0:
            A += 1
        if B % 2 == 0:
            B += 1
        if C % 2 == 0:
            C += 1

    maxValue = max(A, B, C)
    for v in [A, B, C]:
        diff = (maxValue - v)
        answer += diff // 2

    print(answer)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


if __name__ == '__main__':
    main()
