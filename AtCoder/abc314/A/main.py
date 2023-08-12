#!/usr/bin/env python3
import sys

PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"


def solve(N: int):
    print(PI[:N + 2])
    return


def main():
    N = int(sys.stdin.readline().strip())  # type: int
    solve(N)


if __name__ == '__main__':
    main()
