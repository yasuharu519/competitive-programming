#!/usr/bin/env python3

def solve(S: str):
    counter = 0
    wasBlack = S[0] == "B"
    for c in S[1:]:
        if c == "B":
            if wasBlack:
                continue
            else:
                counter += 1
                wasBlack = True
        else:
            if wasBlack:
                counter += 1
                wasBlack = False
            else:
                continue
    print(counter)
    return


def main():
    S = input().strip()
    solve(S)

if __name__ == '__main__':
    main()
