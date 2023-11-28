#!/usr/bin/env python3
import sys

MOD = 2019  # type: int


def solve(L: int, R: int):
    if L == 0:
        print(0)
        return
    passed_l = set()
    passed_r = set()

    result = float('inf')
    for l in range(L, R):
        l_mod = l % 2019
        if l_mod in passed_l:
            continue
        passed_l.add(l_mod)

        passed_r = set()
        for r in range(l+1, R+1):
            r_mod = r % 2019
            if r_mod in passed_r:
                continue
            passed_r.add(r_mod)

            res = (l_mod * r_mod) % 2019
            if res == 0:
                print(0)
                return
            result = min(result, res)
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)

if __name__ == '__main__':
    main()
