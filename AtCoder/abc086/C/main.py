#!/usr/bin/env python3
import sys
from typing import Tuple

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):

    def can_reach(pos: Tuple[int, int], next_pos: Tuple[int, int],
                  time: int) -> bool:
        xi, yi = pos
        xj, yj = next_pos
        diff = abs(xj - xi) + abs(yj - yi)

        if diff == time:
            return True
        elif diff > time:
            return False
        else:
            a = time - diff
            return a % 2 == 0

    current = (0, 0)
    current_time = 0
    for ti, xi, yi, in zip(t, x, y):
        diff = ti - current_time
        res = can_reach(current, (xi, yi), diff)
        if res:
            current = (xi, yi)
            current_time = ti
        else:
            print(NO)
            return
    print(YES)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]"
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, t, x, y)


if __name__ == '__main__':
    main()
