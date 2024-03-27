#!/usr/bin/env python3
import sys
from collections import Counter


def solve(n: int, S: "List[str]"):
    counter = Counter(S[0])

    for s in S[1:]:
        c = Counter(s)

        # merge
        merged = {}
        
        for k in counter.keys():
            if k in c:
                merged[k] = min(counter[k], c[k])
        counter = merged
    
    result = "".join([k*v for k,v in sorted(counter.items())])
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(n)]  # type: "List[str]"
    solve(n, S)

if __name__ == '__main__':
    main()
