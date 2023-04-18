#!/usr/bin/env python3
import sys


def solve(S: str):
    countBlack = 0
    result = 0
    for i in range(len(S)):
        a = S[len(S)-i-1]
        if a == "B":
            result += i - countBlack
            countBlack += 1
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
