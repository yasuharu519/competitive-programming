#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]"):
    if N == M:
        print(sum([x * x for x in A]))
        return

    diff = N - M
    num_of_single = N - 2 * diff

    A.sort(reverse=True)
    res = 0
    index = 0
    while index < N and num_of_single > 0:
        num_of_single -= 1
        res += (A[index]**2)
        index += 1

    left, right = index, N - 1
    while left < right:
        res += ((A[left] + A[right])**2)
        left += 1
        right -= 1

    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()
