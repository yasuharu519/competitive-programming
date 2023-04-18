#!/usr/bin/env python3
import sys


def solve(N: int, x: int, a: "List[int]"):
    a.sort(reverse = True)
    count = 0

    while x > 0 and a:
        popped = a.pop()
        if x >= popped:
            count += 1
        x -= popped
    print(count - 1 if x > 0 else count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x, a)

if __name__ == '__main__':
    main()
