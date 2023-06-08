#!/usr/bin/env python3
import sys


def solve(H: "List[int]"):
    diff = H[0] - H[1]
    print(diff)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    solve(H)

if __name__ == '__main__':
    main()
