#!/usr/bin/env python3
import sys


def solve(N: int, L: int, S: "List[str]"):
    print("".join([x for x in sorted(S)]))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, L, S)


if __name__ == '__main__':
    main()
