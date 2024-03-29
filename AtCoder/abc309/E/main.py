#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(N: int, M: int, p: "List[int]", x: "List[int]", y: "List[int]"):
    covered = [False] * (len(p) + 1)
    coveredMap = defaultdict(int)

    def helper(startNode: int, range: int):
        if range < 0:
            return
        if coveredMap[startNode] > range:
            return
        coveredMap[startNode] = range
        queue = [startNode]
        while queue:
            node = queue.pop()
            covered[node - 1] = True

            for c in [i + 2 for i, v in enumerate(p) if v == node]:
                helper(c, range - 1)

    for xi, yi in sorted(zip(x, y), key=lambda x: x[1], reverse=True):
        helper(xi, yi)

    count = 0
    for c in covered:
        if c:
            count += 1

    print(count)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N - 2 + 1)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, p, x, y)


if __name__ == '__main__':
    main()
