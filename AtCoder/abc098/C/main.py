#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    count = S.count("E")
    result = count
    prev = 0

    for i in range(N):
        if S[i] == "W":
            result = min(result, count + prev)
            prev += 1
        else:
            count -= 1
            result = min(result, count + prev)

    print(result)
    return


def main():
    N = int(input())
    S = input().strip()
    solve(N, S)

if __name__ == '__main__':
    main()
