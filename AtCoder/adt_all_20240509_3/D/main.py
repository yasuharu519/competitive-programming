#!/usr/bin/env python3
from collections import defaultdict

def main():
    N = int(input().strip())
    A = []
    for _ in range(N):
        l = list(map(int, list(input().strip())))
        A.append(l)
    
    d = defaultdict(list)
    for i in range(N):
        for j in range(N):
            d[A[i][j]].append((i, j))
        
    def search(current, direction, v, rest) -> int:
        if rest <= 0:
            return v

        i, j = current
        t = A[i][j]
        v = v * 10 + t

        dx, dy = direction
        xx, yy = i + dx, j + dy
        xx = xx % N
        yy = yy % N
        return search((xx, yy), direction, v, rest-1)
    
    for i in range(10, 0, -1):
        if d[i]:
            points = d[i]
            result = 0
            for x, y in points:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        result = max(result, search((x, y), (dx, dy), 0, N))
            print(result)
            return
    print(0)
    return


if __name__ == '__main__':
    main()
