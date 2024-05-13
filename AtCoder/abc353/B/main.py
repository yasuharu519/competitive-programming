#!/usr/bin/env python3
from collections import deque


def main():
    N, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))

    rest = K
    result = 0
    queue = deque(A)
    while queue:
        while queue and rest >= queue[0]:
            i = queue.popleft()
            rest -= i
        result += 1
        rest = K
    print(result)
    return


if __name__ == '__main__':
    main()
