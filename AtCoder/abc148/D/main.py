#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    if 1 not in a:
        print(-1)
        return
    
    nextTarget = 1
    count = 0
    tmp = 0
    for i, v in enumerate(a):
        if v == nextTarget:
            count += tmp
            tmp = 0
            nextTarget += 1
        else:
            tmp += 1

    count += tmp
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
