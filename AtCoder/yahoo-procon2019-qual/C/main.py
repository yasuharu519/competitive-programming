#!/usr/bin/env python3
import sys


def solve(K: int, A: int, B: int):
    if (B-A <= 2) or (K < A-1):
        print(K+1)
        return
    
    res = A
    K -= (A-1)

    res += (B-A) * (K // 2)
    if (K % 2 == 1):
        res += 1
    
    print(res)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(K, A, B)

if __name__ == '__main__':
    main()
