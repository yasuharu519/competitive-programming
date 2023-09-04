#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, s: "List[str]"):
    for i in range(H):
        for j in range(W):
            if s[i][j] == "#":
                flag = False
                if i > 0:
                    flag = flag or s[i - 1][j] == "#"
                if i < H - 1:
                    flag = flag or s[i + 1][j] == "#"
                if j > 0:
                    flag = flag or s[i][j - 1] == "#"
                if j < W - 1:
                    flag = flag or s[i][j + 1] == "#"
                if not flag:
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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, s)


if __name__ == '__main__':
    main()
