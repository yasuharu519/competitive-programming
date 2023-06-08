#!/usr/bin/env python3
import sys
from collections import Counter


def solve(N: int, S: "List[str]"):
    c = Counter(S)
    s = [(key, value) for key, value in sorted(c.items(), key=lambda x: x[1], reverse=True)]
    key, value = s[0]
    keys = [key]
    for k, v in s[1:]:
        if v == value:
            keys.append(k)
        else:
            break
    
    for key in sorted(keys):
        print(key)


    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
