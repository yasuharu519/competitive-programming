#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H_A: int, W_A: int, A: "List[str]", H_B: int, W_B: int, B: "List[str]", H_X: int, W_X: int, X: "List[str]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H_A = int(next(tokens))  # type: int
    W_A = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(H_A)]  # type: "List[str]"
    H_B = int(next(tokens))  # type: int
    W_B = int(next(tokens))  # type: int
    B = [next(tokens) for _ in range(H_B)]  # type: "List[str]"
    H_X = int(next(tokens))  # type: int
    W_X = int(next(tokens))  # type: int
    X = [next(tokens) for _ in range(H_X)]  # type: "List[str]"
    solve(H_A, W_A, A, H_B, W_B, B, H_X, W_X, X)

if __name__ == '__main__':
    main()
