#!/usr/bin/env python3
import sys


def solve(S: str):
    count1 = 0
    zero = True
    # start 0
    for i in S:
        if (zero == True and i == "1") or (zero == False and i == "0"):
            count1 += 1
        zero = zero ^ True
    
    # start 1
    count2 = 0
    zero = False
    for i in S:
        if (zero == True and i == "1") or (zero == False and i == "0"):
            count2 += 1
        zero = zero ^ True
    
    print(min(count1, count2))
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
