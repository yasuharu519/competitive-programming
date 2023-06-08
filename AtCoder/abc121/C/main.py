#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    drinkPairs = sorted([(x, y) for x, y in zip(A, B)], key=lambda x: x[0])
    requiredMoney = 0
    currentNum = 0

    for price, num in drinkPairs:
        needs = (M - currentNum)
        if num < needs:
            currentNum += num
            requiredMoney += num * price
            continue
        elif num == needs:
            currentNum += num
            requiredMoney += num * price
            break
        else:
            currentNum += needs
            requiredMoney += needs * price
            break

    print(requiredMoney)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
