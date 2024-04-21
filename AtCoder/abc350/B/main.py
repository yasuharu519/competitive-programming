#!/usr/bin/env python3

def main():
    N, Q = list(map(int, input().strip().split()))

    teeth = [1] * N
    T = list(map(int, input().strip().split()))

    for t in T:
        i = t - 1
        if teeth[i] == 0:
            teeth[i] = 1
        else:
            teeth[i] = 0
    print(sum(teeth))


if __name__ == '__main__':
    main()
