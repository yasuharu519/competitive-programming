#!/usr/bin/env python3


def main():
    N, Q = map(int, input().strip().split())
    queries = []
    for _ in range(Q):
        op, c = input().strip().split()
        op = int(op)
        queries.append((op, c))
    
    path = []
    for i in range(N+1, 0, -1):
        p = (i, 0)
        path.append(p)
    
    for op, c in queries:
        if op == 1:
            x, y = path[-1]
            if c == "R":
                x += 1
            elif c == "L":
                x -= 1
            elif c == "U":
                y += 1
            elif c == "D":
                y -= 1
            path.append((x, y))
        else: # 2
            p = int(c)
            x, y = path[-p]
            print("{} {}".format(x, y))
    return

if __name__ == '__main__':
    main()
