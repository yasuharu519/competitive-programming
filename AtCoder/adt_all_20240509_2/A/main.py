#!/usr/bin/env python3

def main():
    N = int(input().strip())
    takahashi, aoki = 0, 0
    for _ in range(N):
        x, y = list(map(int, input().strip().split()))
        takahashi += x
        aoki += y
    
    if takahashi == aoki:
        print("Draw")
    elif takahashi > aoki:
        print("Takahashi")
    else:
        print("Aoki")
    return


if __name__ == '__main__':
    main()
