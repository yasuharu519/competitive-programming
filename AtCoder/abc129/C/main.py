#!/usr/bin/env python3
MOD = 1000000007

def main():
    N, M = list(map(int, input().strip().split()))
    res = [0] * N
    for _ in range(M):
        i = int(input().strip())
        res[i-1] = -1
    
    for i in range(min(2,N)):
        if res[i] != -1:
            res[i] = 1

    for i in range(1, N):
        if res[i] == -1:
            continue
        if i == 1:
            if res[i-1] != -1:
                res[i] += res[i-1]
        else:
            if res[i-2] != -1:
                res[i] += res[i-2]
            if res[i-1] != -1:
                res[i] += res[i-1]
            res[i] = (res[i] % MOD)
    print(res[-1])
    return

if __name__ == '__main__':
    main()
