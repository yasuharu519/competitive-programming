#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: "List[int]"):
    prev = -1
    for v in S:
        if v >= prev and 100 <= v <= 675 and v % 25 == 0:
            prev = v
            continue
        else:
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
    S = [int(next(tokens)) for _ in range(8)]  # type: "List[int]"
    solve(S)

if __name__ == '__main__':
    main()
