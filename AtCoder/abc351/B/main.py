#!/usr/bin/env python3

def main():
    A = []
    B = []

    N = int(input().strip())
    for _ in range(N):
        A.append(input().strip())
    for _ in range(N):
        B.append(input().strip())
    
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                print("{} {}".format(i+1, j+1))
                return
    return

if __name__ == '__main__':
    main()
