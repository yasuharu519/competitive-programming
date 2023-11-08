#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, h: List[int]):
    h0 = h[0]
    if all([x == h0 for x in h]):
        print(h0)
        return
    
    def _solve(l: List[int]) -> int:
        if not l:
            return 0

        min_value = min(l)
        min_index = l.index(min_value)
        cost = min_value
        new_list = [x - min_value for x in l]
        cost += _solve(new_list[0:min_index])
        cost += _solve(new_list[min_index+1:len(l)])
        return cost
    
    cost = 0
    min_value = min(h)
    min_index = h.index(min_value)
    cost += min_value
    for i in range(N):
        h[i] -= min_value
    cost += _solve(h[0:min_index])
    cost += _solve(h[min_index+1:N])
    print(cost)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h)

if __name__ == '__main__':
    main()
