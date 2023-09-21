#!/usr/bin/env python3
import sys
from functools import cache
from typing import List


def solve(N: int):

    @cache
    def generate(num: int) -> List[str]:
        if num % 2 != 0:
            return []
        if num == 0:
            return []
        elif num == 2:
            return ["()"]
        else:
            res = []

            for tmp in generate(num - 2):
                res.append(f"({tmp})")
            for i in range(2, num, 2):
                for left in generate(i):
                    for right in generate(num - i):
                        res.append(f"{left}{right}")
            return res

    res = generate(N)
    print("\n".join(sorted(set(res))))
    return


def main():
    N = int(sys.stdin.readline().strip())
    solve(N)


if __name__ == '__main__':
    main()
