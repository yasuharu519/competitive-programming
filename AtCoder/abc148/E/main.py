#!/usr/bin/env python3
def main():

    N = int(input().strip())

    start = 0
    if N % 2 == 1:
        print(0)
        return
    
    res = 0
    N //= 2

    while N:
        res += N // 5
        N //= 5
    
    print(res)
    return

if __name__ == '__main__':
    main()
