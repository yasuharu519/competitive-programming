#!/usr/bin/env python3
import sys
from collections import Counter


def solve(N: int, a: "List[int]"):
    if not a:
        print(0)
        return
    
    counter = Counter(a)
    result = 0

    for k, v in counter.items():
        if k == v:
            continue
        elif v > k:
            result += (v-k)
            continue
        else:
            result += v
    
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
