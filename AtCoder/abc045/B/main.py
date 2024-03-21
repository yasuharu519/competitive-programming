#!/usr/bin/env python3
import sys


def solve(S_A: str, S_B: str, S_C: str):
    cards = [list(S_A), list(S_B), list(S_C)]
    turn = 0

    while cards[turn]:
        card = cards[turn].pop(0)
        turn = ord(card) - ord('a')
    
    print(chr(ord("A") + turn))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S_A = next(tokens)  # type: str
    S_B = next(tokens)  # type: str
    S_C = next(tokens)  # type: str
    solve(S_A, S_B, S_C)

if __name__ == '__main__':
    main()
