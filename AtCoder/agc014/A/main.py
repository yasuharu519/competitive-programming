#!/usr/bin/env python3
import sys


def willContinue(A: int, B: int, C:int) -> bool:
    return all([x % 2 != 1 for x in [A, B, C]])

def solve(A: int, B: int, C: int):
    count = 0
    passed = set()

    while willContinue(A, B, C):
        if tuple(sorted([A, B, C])) in passed:
            print(-1)
            return
        passed.add(tuple(sorted([A,B,C])))
        A, B, C = (B+C)//2, (A+C)//2, (A+B)//2    
        count += 1
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()
