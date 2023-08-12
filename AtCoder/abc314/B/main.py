#!/usr/bin/env python3
import sys
from typing import List
from collections import defaultdict
import heapq


def solve(N: int, trials: List[List[int]], X: int):
    roulette = {}
    roulette[X] = []

    for i, trial in enumerate(trials):
        v = i + 1
        length = len(trial)
        if X in trial:
            heapq.heappush(roulette[X], (length, v))

    if len(roulette[X]) == 0:
        print(0)
        return
    else:
        length, v = heapq.heappop(roulette[X])
        result = [v]
        while roulette[X]:
            length2, v2 = heapq.heappop(roulette[X])
            if length2 == length:
                result.append(v2)
            else:
                break

        # answer
        print(len(result))
        print(" ".join([str(x) for x in result]))
        return


def main():
    N = int(sys.stdin.readline().strip())
    trials = []
    for _ in range(N):
        _ = int(sys.stdin.readline().strip())
        trials.append(list(map(int, sys.stdin.readline().strip().split())))
    X = int(sys.stdin.readline().strip())
    solve(N, trials, X)
    return


if __name__ == '__main__':
    main()
