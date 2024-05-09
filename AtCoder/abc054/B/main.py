#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N, M = list(map(int, input().strip().split()))
    A = []
    for _ in range(N):
        A.append(input().strip())
    B = []
    for _ in range(M):
        B.append(input().strip())
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            flag = True
            for x in range(M):
                if not flag:
                    break
                for y in range(M):
                    if not flag:
                        break
                    if A[i+x][j+y] != B[x][y]:
                        flag = False
            if flag:
                print(YES)
                return
    print(NO)
    return



if __name__ == '__main__':
    main()
