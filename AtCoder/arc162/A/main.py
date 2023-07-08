#!/usr/bin/env python3
import sys
from typing import List



def solve(Ps: List[List[int]]):
    for p in Ps:
        l = [(v, i+1) for i, v in enumerate(p)]
        current_max, start_max = -1, -1
        l.sort()

        count = 0
        for c, s in l:
            if c <= s and c > current_max and s > start_max:
                count += 1
                current_max = c
                start_max = s
        print(count)






def main():
    # Failed to predict input format
    T = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(T):
        _ = sys.stdin.readline().strip()
        cases.append([int(x) for x in sys.stdin.readline().strip().split()])
    solve(cases)
        
    pass

if __name__ == '__main__':
    main()
