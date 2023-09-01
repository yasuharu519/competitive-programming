#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(S: str):
    n = len(S)
    if S == "keyence":
        print(YES)
        return

    for i in range(n - 1):
        for j in range(i + 1, n):
            if S[:i] + S[j:] == "keyence":
                print(YES)
                return
    print(NO)
    return


def main():
    S = sys.stdin.readline().strip()
    solve(S)


if __name__ == '__main__':
    main()
