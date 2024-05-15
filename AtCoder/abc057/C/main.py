#!/usr/bin/env python3
def main():
    N = int(input().strip())

    i = 1
    result = float('inf')
    while i * i <= N:
        if N % i == 0:
            j = N // i
            result = min(result, max(len(str(i)), len(str(j))))
        i += 1
    print(result)

if __name__ == '__main__':
    main()
