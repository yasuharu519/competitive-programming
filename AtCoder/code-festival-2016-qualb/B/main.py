#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: int, B: int, S: str):
    passCount = 0
    passOverseas = 0
    result = []

    for i in S:
        if i == "a":
            if passCount < (A+B):
                passCount += 1
                result.append(YES)
            else:
                result.append(NO)
        elif i == "b":
            if passCount < (A+B) and passOverseas < B:
                passCount += 1
                passOverseas += 1
                result.append(YES)
            else:
                result.append(NO)
        else:
            result.append(NO)
    
    print("\n".join(result))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    S = next(tokens)  # type: str

    solve(N, A, B, S)


if __name__ == '__main__':
    main()
