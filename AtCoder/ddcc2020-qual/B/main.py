#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    total = sum(A)
    minimum = total

    currentSum = 0
    for v in A[:-1]:
        currentSum += v
        diff = total - currentSum

        minimum = min(minimum, abs(currentSum - diff))

    print(minimum)
    return


def main():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    solve(N, A)


if __name__ == '__main__':
    main()
