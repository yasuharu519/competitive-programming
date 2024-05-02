#!/usr/bin/env python3
def main():
    S = input().strip()
    N = len(S)

    dp = [[0] * N for _ in range(33)]
    ans = [0] * N

    for i in range(N):
        if S[i] == 'R':
            dp[0][i] = i + 1 if i + 1 < N else i
        else:
            dp[0][i] = i - 1 if i - 1 >= 0 else i
    
    for p in range(32):
        for i in range(N):
            dp[p + 1][i] = dp[p][dp[p][i]]
    for i in range(N):
        ans[dp[32][i]] += 1
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()
