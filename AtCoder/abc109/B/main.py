#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, W: "List[str]"):
    current = W[0]
    passed = set()
    passed.add(current)

    for w in W[1:]:
        if w in passed:
            print(NO)
            return
        if w[0] != current[-1]:
            print(NO)
            return
        passed.add(w)
        current = w
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, W)

if __name__ == '__main__':
    main()
