#!/usr/bin/env python3
import sys

def dist(xs) -> int:
    ans = 0
    n = len(xs)
    for j in range(n):
        ans += (2 * j + 1 - n) * xs[j]
    return ans

def main():
    N = int(input().strip())

    e_e_x = []
    e_e_y = []
    o_e_x = []
    o_e_y = []

    result = 0

    for _ in range(N):
        x, y = list(map(int, input().strip().split()))
        if (x+y) % 2 == 0:
            e_e_x.append(x+y)
            e_e_y.append(x-y)
        else:
            o_e_x.append(x+y)
            o_e_y.append(x-y)
    e_e_x.sort()
    e_e_y.sort()
    o_e_x.sort()
    o_e_y.sort()

    result += dist(e_e_x)
    result += dist(e_e_y)
    result += dist(o_e_x)
    result += dist(o_e_y)
    print(result//2)
    return


if __name__ == '__main__':
    main()
