#!/usr/bin/env python3
import sys


def solve(S: str):
    stack = []

    for s in S:
        if s == "C":
            while len(stack) >= 2 and stack[-1] == "B" and stack[-2] == "A":
                stack.pop()
                stack.pop()
                break
            else:
                stack.append(s)
        else:
            stack.append(s)

    print("".join(stack))
    return


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
