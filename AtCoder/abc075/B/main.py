#!/usr/bin/env python3
import sys


def solve(H: int, W: int, S: "List[str]"):
    ans = [[0] * W for _ in range(H)]

    def check(x: int, y: int):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif x + i < 0 or x + i >= H or y + j < 0 or y + j >= W:
                    continue
                elif S[x + i][y + j] == "#":
                    continue
                else:
                    ans[x + i][y + j] += 1

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                check(i, j)

    for i in range(H):
        print("".join(
            ["#" if S[i][j] == "#" else str(v) for j, v in enumerate(ans[i])]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == '__main__':
    main()
