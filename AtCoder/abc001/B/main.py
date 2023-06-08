#!/usr/bin/env python3
import sys

MOD = 5  # type: int


def getvv(m: int) -> str:
    if m > 70000:
        return 89
    elif 35000 <= m <= 70000:
        return ((m // 1000) - 30) // 5 + 80
    elif 6000 <= m <= 30000:
        return m // 1000 + 50
    elif 100 <= m <= 5000:
        return "{:02}".format(int((m / 1000) * 10))
    else:
        return "00"

def solve(m: int):
    print(getvv(m))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    m = int(next(tokens))  # type: int
    solve(m)

if __name__ == '__main__':
    main()
