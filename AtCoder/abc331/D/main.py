#!/usr/bin/env python3
import sys


def main():
    N, Q = [int(x) for x in input().strip().split()]
    P = []
    for _ in range(N):
        P.append(input().strip())
    
    count_list = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            count = 1 if P[i-1][j-1] == "B" else 0
            if i == 0 and j == 0:
                count_list[i][j] = count
            elif i == 0:
                count_list[i][j] = count_list[i][j-1] + count
            elif j == 0:
                count_list[i][j] = count_list[i-1][j] + count
            else:
                count_list[i][j] = count_list[i-1][j] + count_list[i][j-1] + count - count_list[i-1][j-1]
    
    def g(H: int, W: int) -> int:
        if (H <= N and W <= N):
            return count_list[H][W]
        hq, hr = divmod(H, N)
        wq, wr = divmod(W, N)

        ans = 0
        ans += g(N, N) * hq * wq
        ans += g(hr, N) * wq
        ans += g(N, wr) * hq
        ans += g(hr, wr)
        return ans
    

    for _ in range(Q):
        A, B, C, D = [int(x) for x in input().strip().split()]
        C, D = C+1, D+1
        print(g(C, D) - g(A, D) - g(C, B) + g(A, B))
    


if __name__ == '__main__':
    main()
