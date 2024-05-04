#!/usr/bin/env python3

def main():
    H, W = list(map(int, input().strip().split()))
    s = []
    for _ in range(H):
        s.append(input().strip())
    
    dp = [[float('inf')] * W for _ in range(H)]

    dp[0][0] = 1 if s[0][0] == "#" else 0

    for i in range(H):
        for j in range(W):
            for dx, dy in [(1, 0), (0, 1)]:
                xx, yy = i + dx, j + dy
                if xx >= H or yy >=W:
                    continue
                add = 1 if (s[xx][yy] == "#" and s[i][j] == ".") else 0
                dp[xx][yy] = min(dp[xx][yy], dp[i][j] + add)
    
    print(dp[H-1][W-1])
    return

if __name__ == '__main__':
    main()
