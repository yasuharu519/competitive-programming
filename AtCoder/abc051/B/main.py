#!/usr/bin/env python3

def main():
    K, S = list(map(int, input().strip().split()))
    count = 0

    for x in range(K+1):
        for y in range(K+1):
            total = x + y
            diff = S - total
            if 0 <= diff <= K:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
