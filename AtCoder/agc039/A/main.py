#!/usr/bin/env python3
import sys


def solve(S: str, K: int):

    rle = []
    n = len(S)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and S[i] == S[i + 1]:
            i += 1
            count += 1
        rle.append((S[i], count))
        i += 1
    
    if S[0] == S[-1]:
        if len(rle) == 1:
            print((rle[0][1] * K) // 2)
        else:
            a = rle.pop(0)[1]
            b = rle.pop()[1]
            total = sum([x[1] // 2 for x in rle]) * K
            total += (a // 2 + b // 2 + ((a+b) // 2)*(K-1))
            print(total)
    else:
        total = sum([x[1] // 2 for x in rle])
        print(total * K)
    return


# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)

if __name__ == '__main__':
    main()
