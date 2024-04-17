#!/usr/bin/env python3
import sys


def solve(x: int):
    count = (x // 11) * 2
    rest = x - 11 * (count // 2)
    if rest > 0:
        count += 1
        rest -= 6
    if rest > 0:
        count += 1
        rest -= 5
    print(count)
    return


def main():
    x = int(input().strip())
    solve(x)

if __name__ == '__main__':
    main()
