#!/usr/bin/env python3

from typing import List

def solve(UD: str):
    result = 0
    N = len(UD)
    for i, c in enumerate(UD):
        if c == "U":
            # up
            result += (N - 1 - i)
            # down
            result += i * 2
        else:
            # down
            result += i
            # up
            result += (N - 1 - i) * 2

    print(result)
    pass

def main():
    UD = input().strip()
    solve(UD)

if __name__ == '__main__':
    main()
