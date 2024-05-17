#!/usr/bin/env python3

def gcd(A: int, B: int) -> int:
    while B != 0:
        A, B = B, A % B
    return A

def main():
    A, B = list(map(int, input().strip().split()))

    G = gcd(A, B)

    # 1 は必ず含む
    count = 1
    if G % 2 == 0:
        count += 1
        while G % 2 == 0:
            G //= 2
    i = 3
    while i * i <= G:
        if G % i == 0:
            count += 1
            while G % i == 0:
                G //= i
        i += 2
    if G != 1:
        count += 1
    print(count)

if __name__ == '__main__':
    main()
