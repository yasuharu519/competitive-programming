#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    result = []
    counter = 0

    for a in A:
        if counter % 7 == 0:
            result.append(0)
        result[-1] += a
        counter += 1
    
    print(" ".join([str(x) for x in result]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(7 * N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
