#!/usr/bin/env python3
import sys

def calc(H: int) -> int:
    if H == 1:
        return 1
    return 1 + 2 * calc(H // 2)

def solve(H: int):
    print(calc(H))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    solve(H)

if __name__ == '__main__':
    main()
