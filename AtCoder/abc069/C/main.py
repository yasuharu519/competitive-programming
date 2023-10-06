#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, a: "List[int]"):
    count4 = 0
    count2 = 0
    count1 = 0

    for v in a:
        if v % 4 == 0:
            count4 += 1
        elif v % 2 == 0:
            count2 += 1
        else:
            count1 += 1

    if count1 <= count4:
        print(YES)
    elif count1 == count4 + 1 and count2 == 0:
        print(YES)
    else:
        print(NO)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
