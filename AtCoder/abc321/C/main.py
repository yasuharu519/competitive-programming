#!/usr/bin/env python3
import sys


def isValidNumber(num: int) -> bool:
    if num == 0:
        return False
    elif 0 < num < 10:
        return True

    strN = str(num)
    current = strN[0]
    for i in range(1, len(strN)):
        if int(current) <= int(strN[i]):
            return False
        current = strN[i]
    return True


def generator():
    num = 1
    while True:
        if isValidNumber(num):
            yield num
        num += 1


def solve(K: int):
    gen = generator()
    count = 0
    for number in gen:
        count += 1
        if count == K:
            print(number)
            return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()
