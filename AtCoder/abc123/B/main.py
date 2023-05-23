#!/usr/bin/env python3
import sys
from itertools import permutations

def solve(A: int, B: int, C: int, D: int, E: int):
    answer = float('inf')
    for L in list(permutations([A, B, C, D, E])):
        sum = 0
        for i in range(5):
            sum += L[i]
            if (i < 4):
                sum += (10 - sum % 10) % 10
        answer = min(answer, sum)
    print(answer)
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
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(A, B, C, D, E)

if __name__ == '__main__':
    main()
