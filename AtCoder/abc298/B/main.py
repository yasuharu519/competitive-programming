# coding:utf-8
import sys
from typing import List


def solve(N: int, A: List[List[int]], B: List[List[int]]):
    result = False
    oneIndex = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                oneIndex.append((i, j))

    result = False
    # 通常ケース
    tmpResult = True
    for x, y in oneIndex:
        if B[x][y] != 1:
            tmpResult = False
            break
    result = result or tmpResult

    # 1度目の回転
    if not result:
        tmpResult = True
        for x, y in oneIndex:
            if B[y][N - x - 1] != 1:
                tmpResult = False
                break
        result = result or tmpResult
    # 2度目の回転
    if not result:
        tmpResult = True
        for x, y in oneIndex:
            if B[N - x - 1][N - y - 1] != 1:
                tmpResult = False
                break
        result = result or tmpResult
    # 3度目の回転
    if not result:
        tmpResult = True
        for x, y in oneIndex:
            if B[N - y - 1][x] != 1:
                tmpResult = False
                break
        result = result or tmpResult

    print("Yes" if result else "No")
    return


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(N)]
    B = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(N)]

    solve(N, A, B)
