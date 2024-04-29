#!/usr/bin/env python3
from pprint import pprint

def main():
    H, W = list(map(int, input().strip().split()))
    S = []
    for _ in range(H):
        S.append(input().strip())
    grid = [[0] * W for _ in range(H)]
    result = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                grid[i][j] = -1
                result[i][j] = -1
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    xx, yy = i + dx, j + dy
                    if 0 <= xx < H and 0 <= yy < W and S[xx][yy] != "#":
                        grid[xx][yy] = 1
                        result[xx][yy] = 1
    
    max_result = 1
    for i in range(H):
        for j in range(W):
            if result[i][j] == 0:
                # dfs start
                start = (i, j)
                same_group = set()
                passed = set()
                queue = [start]
                while queue:
                    x, y = queue.pop()
                    if (x, y) in passed:
                        continue
                    passed.add((x, y))
                    if result[x][y] == 1:
                        continue
                    elif result[x][y] == 0:
                        same_group.add((x, y))
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < H and 0 <= yy < W and result[xx][yy] != -1 and (xx, yy) not in passed:
                            queue.append((xx, yy))
                l = len(passed)
                max_result = max(max_result, l)
                for x, y in same_group:
                    result[x][y] = l
    print(max_result)
    return

if __name__ == '__main__':
    main()
