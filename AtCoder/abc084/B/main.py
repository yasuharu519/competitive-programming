#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: int, B: int, S: str):
    if S[A] != "-":
        print(NO)
        return
    
    for i in S[:A]:
        if i not in "0123456789":
            print(NO)
            return
    for i in S[A+1:]:
        if i not in "0123456789":
            print(NO)
            return
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(A, B, S)

if __name__ == '__main__':
    main()
