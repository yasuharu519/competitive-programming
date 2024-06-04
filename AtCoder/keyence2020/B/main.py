#!/usr/bin/env python3
def main():
    N = int(input().strip())
    arms = []
    for _ in range(N):
        x, l = map(int, input().strip().split())
        arms.append((x - l, x + l))
    
    arms.sort(key=lambda x: x[1])
    res = 0
    current = float('-inf')
    for l, r in arms:
        if current > l:
            continue
        res += 1
        current = r
    print(res)

if __name__ == '__main__':
    main()
