#!/usr/bin/env python3
import sys
import math


def get_pos(T: int, L: int, E: int) -> (float, float, float):
    mod = E % T
    radian = 2 * math.pi * mod / T
    return (0, -1 * (L / 2) * math.sin(radian), L / 2 * (1 - math.cos(radian)))


def solve(T: int, L: int, X: int, Y: int, Q: int, E: "List[int]"):

    for e in E:
        x, y, z = get_pos(T, L, e)
        dis = math.sqrt((X - x)**2 + (Y - y)**2)

        r = math.atan(z / dis)
        print(r * 360 / (2 * math.pi))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    E = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(T, L, X, Y, Q, E)


if __name__ == '__main__':
    main()
