#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    count = 0
    for i in range(len(B)-1, -1, -1):
        beat = B[i]

        if A[i+1] <= beat:
            beat -= A[i+1]
            count += A[i+1]
            A[i+1] = 0
        else:
            count += beat
            A[i+1] -= beat
            beat = 0
        
        if A[i] <= beat:
            beat -= A[i]
            count += A[i]
            A[i] = 0
        else:
            count += beat
            A[i] -= beat
            beat = 0
    
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
