#!/usr/bin/env python3
from atcoder.segtree import SegTree
import bisect

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    B = sorted(list(set(A)))
    M = len(B)

    sum_count = SegTree(lambda x, y: x+y, 0, M)
    sum_total = SegTree(lambda x, y: x+y, 0, M)

    ans = 0
    for i in reversed(range(N)):
        k = bisect.bisect_left(B, A[i])
        c = sum_count.prod(k, M)
        s = sum_total.prod(k, M)
        ans += s - c * A[i]
        a = sum_count.get(k)
        b = sum_total.get(k)
        sum_count.set(k, a+1)
        sum_total.set(k, b+A[i])
    print(ans)


if __name__ == '__main__':
    main()
