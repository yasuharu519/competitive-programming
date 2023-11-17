#!/usr/bin/env python3
import sys
from collections import deque


def solve(n: int, a: "List[int]"):
    queue = deque()
    for i, v in enumerate(a):
        if i % 2 == 0:
            queue.append(v)
        else:
            queue.appendleft(v)
    if n % 2 == 0:
        print(" ".join(map(str, queue)))
    else:
        print(" ".join(map(str, reversed(queue))))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
