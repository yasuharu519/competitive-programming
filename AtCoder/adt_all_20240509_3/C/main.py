#!/usr/bin/env python3

def main():
    H, W = list(map(int, input().strip().split()))

    result = []
    for _ in range(H):
        l = list(map(int, input().strip().split()))
        result.append("".join([chr(x - 1 + ord('A')) if x != 0 else "." for x in l]))

    for l in result:
        print(l)

if __name__ == '__main__':
    main()
