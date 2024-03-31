#!/usr/bin/env python3
import sys


def solve(x: int, y: int):
    if x == y:
        print(0)
        return

    if abs(x) == abs(y):
        print(1)
        return
    
    if x > 0 and y > 0:
        if x < y:
            print(y - x)
        else:
            print(x - y + 2)
    elif x < 0 and y < 0:
        if x < y:
            print(abs(x) - abs(y))
        else:
            print(abs(y) - abs(x) + 2)
    elif x == 0:
        if y > 0:
            print(y)
        else:
            print(abs(y) + 1)
    elif y == 0:
        if x > 0:
            print(x + 1)
        else:
            print(abs(x))
    else:
        print(abs(abs(y)-abs(x)) + 1)
    return


def main():
    x, y = list(map(int, input().strip().split()))
    solve(x, y)

if __name__ == '__main__':
    main()
