#!/usr/bin/env python3
def main():
    a, b, x = list(map(int, input().strip().split()))

    l = (a + x - 1) // x
    r = b // x

    print(r - l + 1)
    return

if __name__ == '__main__':
    main()
