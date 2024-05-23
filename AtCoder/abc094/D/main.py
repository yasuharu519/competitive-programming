#!/usr/bin/env python3
def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    A.sort()

    ai = A[N-1]
    aj = A[0]
    for i in range(N-1):
        if abs(A[i] - ai / 2) <= abs(aj-ai/2):
            aj = A[i]
    print(f"{ai} {aj}")


if __name__ == '__main__':
    main()
