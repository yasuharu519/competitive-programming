#!/usr/bin/env python3

import sys
from typing import List


def solve(H: int, W: int, C: List[List[str]]):

    queue = []
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                queue.append((i, j))

    N = min(H, W)
    result = [0 for x in range(N)]

    def check(x: int, y: int):
        # 左上に
        if x == 0 or y == 0:
            return
        count = 0
        current = (x - 1, y - 1)
        while current[0] >= 0 and current[1] >= 0 and C[current[0]][
                current[1]] == "#":
            count += 1
            current = current[0] - 1, current[1] - 1

        if count == 0:
            return

        # ほか方向をチェック
        for i in range(1, count + 1):
            rightUp = (x - i, y + i)
            rightDown = (x + i, y + i)
            leftDown = (x + i, y - i)

            if x - i < 0 or x + i >= H or y - i < 0 or y + i >= W:
                return

            if any([
                    C[rightUp[0]][rightUp[1]] != "#",
                    C[rightDown[0]][rightDown[1]] != "#",
                    C[leftDown[0]][leftDown[1]] != "#"
            ]):
                return

        result[count - 1] += 1
        return

    for q in queue:
        check(q[0], q[1])
    print(" ".join([str(x) for x in result]))
    pass


def main():
    # Failed to predict input format
    H, W = [int(x) for x in sys.stdin.readline().strip().split()]
    C = []
    for _ in range(H):
        C.append(list(sys.stdin.readline().strip()))

    solve(H, W, C)
    pass


if __name__ == '__main__':
    main()
