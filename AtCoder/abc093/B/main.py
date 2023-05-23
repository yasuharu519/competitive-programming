#!/usr/bin/env python3
import sys


def solve(A: int, B: int, K: int):
    # from small to large
    list1 = list(range(A, A+K))
    list2 = list(range(B-K+1, B+1))
    final = list(sorted(set(list1+list2)))
    for i in final:
        if i < A or i > B:
            continue
        print(i)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, K)

if __name__ == '__main__':
    main()
