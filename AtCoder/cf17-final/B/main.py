#!/usr/bin/env python3
import sys
from collections import Counter

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(S: str):
    counter = Counter(S)
    count = {"a": 0, "b": 0, "c": 0}
    for k, v in counter.items():
        count[k] = v
    
    values = list(count.values())
    values.sort()

    val = values[0]
    for v in values[1:]:
        if v > val + 1:
            print(NO)
            return
    print(YES)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
