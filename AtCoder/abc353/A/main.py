#!/usr/bin/env python3
def main():
    N = int(input().strip())
    H = list(map(int, input().strip().split()))

    first = H[0]
    for i, h in enumerate(H[1:]):
        index = i + 2
        if h > first:
            print(index)
            return
    print(-1)
    return


if __name__ == '__main__':
    main()
