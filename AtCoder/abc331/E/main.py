#!/usr/bin/env python3
import sys


def solve(N: int, M: int, L: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    blist = []
    for i, x in enumerate(b):
        blist.append((x, i))
    blist.sort(reverse=True)

    avoid_list = set()
    for x, y in zip(c, d):
        avoid_list.add((x-1, y-1))
    
    ans = 0
    for i, x in enumerate(a):
        for y, j in blist:
            if (i, j) in avoid_list:
                continue
            ans = max(ans, x+y)
            break
    print(ans)
    return

# 40, 30, 20
# [0, -10, -10]
# 100, 90, 10
# [0, -10, -80]



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    c = [int()] * (L)  # type: "List[int]"
    d = [int()] * (L)  # type: "List[int]"
    for i in range(L):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, M, L, a, b, c, d)

if __name__ == '__main__':
    main()
