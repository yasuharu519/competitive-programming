#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, S: str, l: "List[int]", r: "List[int]"):
    prefix = [0]
    counter = 0
    for i in range(1, N):
        if S[i-1] == S[i]:
            counter += 1
        prefix.append(counter)
    
    for left, right in zip(l, r):
        print(prefix[right-1] - prefix[left-1])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, S, l, r)

if __name__ == '__main__':
    main()
