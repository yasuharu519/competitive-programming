#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import combinations

def solve(N: int, S: "List[str]"):
    counter = defaultdict(int)

    for s in S:
        if s[0] in "MARCH":
            counter[s[0]] += 1
    
    result = 0
    for choice in combinations("MARCH", 3):
        result += (counter[choice[0]] * counter[choice[1]] * counter[choice[2]])
    print(result)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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