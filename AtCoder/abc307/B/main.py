#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, S: "List[str]"):
    passed = set()

    for v in S:
        if v[::-1] in passed:
            print(YES)
            return
        
        passed.add(v)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
