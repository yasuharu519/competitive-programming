#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: int, B: int, C: int, D: int, S: str):
    A, B, C, D = A-1, B-1, C-1, D-1
    if "##" in S[A:C+1] or "##" in S[B:D+1]:
        print(NO)
        return
    
    if C < D:
        print(YES)
        return
    
    if "..." in S[B-1:D+2]:
        print(YES)
    else:
        print(NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, A, B, C, D, S)

if __name__ == '__main__':
    main()
