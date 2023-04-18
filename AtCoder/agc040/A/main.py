#!/usr/bin/env python3
import sys


def solve(S: str):
    current = 0
    result = 0
    smallest = 0

    for i in S:
        if i == "<":
            current += 1
        else:
            current -= 1
        result += current
        smallest = min(smallest, current)
    result += current
    
    if smallest < 0:
        diff = 0 - smallest
        result += diff * (len(S) + 1)
    print(result)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
