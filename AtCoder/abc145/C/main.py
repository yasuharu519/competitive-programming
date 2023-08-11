#!/usr/bin/env python3
import sys
import math
from itertools import permutations


def calc_distance(points: "List[List[int]]") -> float:
    n = len(points)
    distance = 0
    for i in range(1, n):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def solve(N: int, x: "List[int]", y: "List[int]"):
    points = [(i, j) for i, j in zip(x, y)]
    perms = permutations(points)
    count = 0
    total = 0
    for perm in perms:
        count += 1
        total += calc_distance(perm)
    print(total / count)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


if __name__ == '__main__':
    main()
