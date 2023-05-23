#!/usr/bin/env python3
import sys


def solve(S: int):
    s = str(S)
    diff = float('inf')

    for i in range(len(s[:-2])):
        num = int(s[i:i+3])
        diff = min(diff, abs(num-753))
    
    print(diff)
        
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()
