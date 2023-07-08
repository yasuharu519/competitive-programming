#!/usr/bin/env python3
import sys
from functools import cmp_to_key

def solve(N: int, A: "List[int]", B: "List[int]"):
    people = [(i+1, A[i], B[i]) for i in range(N)]

    def cmp(left, right):
        li, la, lb = left
        ri, ra, rb = right
        leftCal, rightCal = la * (ra + rb), ra * (la + lb)
        if leftCal == rightCal:
            if li <= ri:
                return -1
            else:
                return 1
        elif leftCal < rightCal:
            return 1
        else:
            return -1

    sortedList = sorted(people, key=cmp_to_key(cmp))
    print(" ".join([str(x[0]) for x in sortedList]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
