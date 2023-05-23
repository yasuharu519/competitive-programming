#!/usr/bin/env python3
import sys


def solve(x: "List[int]", y: "List[int]"):
    x1, y1 = x[0], y[0]
    x2, y2 = x[1], y[1]

    v1 = (x2-x1, y2-y1)
    v2 = (-1*v1[1], v1[0])

    x3, y3 = x2+v2[0], y2+v2[1]
    x4, y4 = x1+v2[0], y1+v2[1]

    print(x3, y3, x4, y4)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [int()] * (2)  # type: "List[int]"
    y = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(x, y)

if __name__ == '__main__':
    main()
