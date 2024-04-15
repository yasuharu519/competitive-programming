#!/usr/bin/env python3
from typing import List, Dict
from collections import Counter

YES = "Yes"
NO = "No"

def solve(N: int, a: List[int]) -> bool:
    counter = Counter(a)

    if N % 3 != 0:
        return counter.get(0, 0) == N
    v = list(counter.keys())
    if len(v) == 1:
        return counter.get(0, 0) == N
    elif len(v) == 2:
        return counter.get(0, 0) == N // 2
    elif len(v) == 3:
        if (v[0] ^ v[1] ^ v[2]) != 0:
            return False
        return (counter[v[0]] == N // 3 and counter[v[1]] == N // 3 and counter[v[2]] == N // 3)
    else:
        return False

def main():
    N = int(input().strip())
    a = list(map(int, input().strip().split()))
    print(YES if solve(N, a) else NO)

if __name__ == '__main__':
    main()
