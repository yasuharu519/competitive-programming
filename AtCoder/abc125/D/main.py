#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().strip().split()))

    total = 0
    min_value = float('inf')
    odd = False
    for a in A:
        if a < 0:
            odd = not odd
        min_value = min(min_value, abs(a))
        total += abs(a)
    
    if odd:
        total -= min_value * 2
    print(total)


if __name__ == '__main__':
    main()
