#!/usr/bin/env python3
import sys
from typing import List, Tuple

YES = "Yes"  # type: str
NO = "No"  # type: str


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] <= self.rank[root_y]:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def solve(H: int, W: int, Q: int, Qs: List[int]):
    red_map = [[False] * W for _ in range(H)]
    uf = UnionFind(H * W)

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for q in Qs:
        op, nums = q[0], q[1:]
        if op == 1:
            r, c = nums
            r -= 1
            c -= 1
            red_map[r][c] = True

            for dx, dy in directions:
                next_x, next_y = r + dx, c + dy
                if 0 <= next_x < H and 0 <= next_y < W and red_map[next_x][
                        next_y]:
                    from_index = r * W + c
                    to_index = next_x * W + next_y
                    uf.union(from_index, to_index)
        else:
            r1, c1, r2, c2 = nums
            r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

            if red_map[r1][c1] == False or red_map[r2][c2] == False:
                print(NO)
                continue

            from_index = r1 * W + c1
            to_index = r2 * W + c2

            res = uf.same(from_index, to_index)
            print(YES if res else NO)


def main():
    H, W = list(map(int, sys.stdin.readline().strip().split()))
    Q = int(sys.stdin.readline().strip())
    Qs = []
    for line in sys.stdin.readlines():
        Qs.append(list(map(int, line.split())))

    solve(H, W, Q, Qs)
    pass


if __name__ == '__main__':
    main()
