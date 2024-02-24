#!/usr/bin/env python3
from collections import defaultdict

def main():
    N = int(input())
    S = input().strip()
    Q = int(input())
    cd = []
    change_map = {chr(i+ord('a')): chr(i+ord('a')) for i in range(26)}
    for _ in range(Q):
        c, d = input().strip().split()
        if c == d:
            continue

        for char, mapped in change_map.items():
            if mapped == c:
                change_map[char] = d

    result = []
    for c in S:
        if c in change_map:
            result.append(change_map[c])
        else:
            result.append(c)
    print("".join(result))


    


if __name__ == '__main__':
    main()
