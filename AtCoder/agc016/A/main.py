#!/usr/bin/env python3
import sys
from collections import Counter


def solve(s: str):
    char_set = set(s)
    
    result = float('inf')

    for target in char_set:
        char_result = 0
        count = 0
        for c in s:
            if c == target:
                char_result = max(char_result, count)
                count = 0
            else:
                count += 1
        char_result = max(char_result, count)
        result = min(result, char_result)
    
    print(result)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()