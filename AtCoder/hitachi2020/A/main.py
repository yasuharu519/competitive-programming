#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    if "hi" == S:
        print(YES)
    elif "hihi" == S:
        print(YES)
    elif "hihihi" == S:
        print(YES)
    elif "hihihihi" == S:
        print(YES)
    elif "hihihihihi" == S:
        print(YES)
    else:
        print(NO)
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
