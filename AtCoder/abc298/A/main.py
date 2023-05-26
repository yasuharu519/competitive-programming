# coding:utf-8
import sys


def solve(N: int, S: str):
    has_good = False
    has_bad = False

    for i in S:
        if i == 'o':
            has_good = True
        elif i == "x":
            has_bad = True

    print("Yes" if has_good and not has_bad else "No")
    return


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()

    solve(N, S)
