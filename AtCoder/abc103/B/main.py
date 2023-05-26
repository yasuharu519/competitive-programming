#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    if S == T:
        print(YES)
        return
    n = len(S)
    for i in range(1, n):
        if S[i:] + S[:i] == T:
            print(YES)
            return
    print(NO)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == '__main__':
    main()
