#!/usr/bin/env python3
def main():
    H, W, N = list(map(int, input().strip().split()))
    T = input().strip()
    S = []
    for _ in range(H):
        S.append(input().strip())


    def can_pass(x, y) -> bool:
        cx = x
        cy = y

        for i in T:
            if i == "L":
                cy -= 1
            elif i == "R":
                cy += 1
            elif i == "U":
                cx -= 1
            else:
                cx += 1
            if cx <= 0 or cy <= 0 or cx >= H-1 or cy >= W-1 or S[cx][cy] == "#":
                return False
        return True

    
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "." and can_pass(i, j):
                count += 1
    print(count)
    return


if __name__ == '__main__':
    main()
