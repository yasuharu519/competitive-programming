#!/usr/bin/env python3
from collections import Counter

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = [-1] * N

    for i, a in enumerate(A):
        B[a-1] = i

    result = []
    for i in range(N):
        a, b = A[i], B[i]
        if i + 1 == a:
            continue
        result.append((i+1, b+1))
        A[i], A[b] = A[b], A[i]
        B[a-1] = b
    
    print(len(result))
    for r in result:
        print("{} {}".format(r[0], r[1]))



if __name__ == '__main__':
    main()
