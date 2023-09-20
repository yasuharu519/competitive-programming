#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(c: "List[List[int]]"):
    row_diff = [c[0][1] - c[0][0], c[0][2] - c[0][1]]
    col_diff = [c[1][0] - c[0][0], c[2][0] - c[1][0]]

    for i in range(1, 3):
        diff = [c[i][1] - c[i][0], c[i][2] - c[i][1]]
        if diff != row_diff:
            print(NO)
            return
    for j in range(1, 3):
        diff = [c[1][j] - c[0][j], c[2][j] - c[1][j]]
        if diff != col_diff:
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
    c = [[int(next(tokens)) for _ in range(3)]
         for _ in range(3)]  # type: "List[List[int]]"
    solve(c)


if __name__ == '__main__':
    main()
