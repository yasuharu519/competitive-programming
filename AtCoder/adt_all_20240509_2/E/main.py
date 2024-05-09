#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N = int(input().strip())
    S = []
    for _ in range(N):
        l = input().strip()
        S.append([x for x in l])

    def is_connected() -> bool:
        for i in range(N-6+1):
            for j in range(N-6+1):
                # tate
                if all([S[i+x][j] == "#" for x in range(6)]):
                    return True
                # yoko
                if all([S[i][j+x] == "#" for x in range(6)]):
                    return True
                if all(S[i+x][j+x] == "#" for x in range(6)):
                    return True
                if all(S[i+5-x][j+x] == "#" for x in range(6)):
                    return True
        return False
    
    def backtrack(N, x, y) -> bool:

        for i in range(x, N):
            for j in range(N):
                if i == x and j <= y:
                    continue

                if S[i][j] == ".":
                    S[i][j] = "#"
                    if is_connected():
                        return True
                    S[i][j] = "."
        return False
    
    if is_connected():
        print(YES)
        return


    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i][j] = "#"
                if backtrack(N, i, j):
                    print(YES)
                    return
                S[i][j] = "."
    print(NO)
    return

if __name__ == '__main__':
    main()
