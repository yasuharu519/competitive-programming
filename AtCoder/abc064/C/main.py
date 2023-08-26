#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    colors = {
        "gray": 0,
        "brown": 0,
        "green": 0,
        "aqua": 0,
        "blue": 0,
        "yellow": 0,
        "orange": 0,
        "red": 0,
        "wild": 0
    }

    for v in a:
        if 1 <= v <= 399:
            colors["gray"] += 1
        elif 400 <= v <= 799:
            colors["brown"] += 1
        elif 800 <= v <= 1199:
            colors["green"] += 1
        elif 1200 <= v <= 1599:
            colors["aqua"] += 1
        elif 1600 <= v <= 1999:
            colors["blue"] += 1
        elif 2000 <= v <= 2399:
            colors["yellow"] += 1
        elif 2400 <= v <= 2799:
            colors["orange"] += 1
        elif 2800 <= v <= 3199:
            colors["red"] += 1
        else:
            colors["wild"] += 1

    num_colors = 0
    for k, v in colors.items():
        if k == "wild":
            continue
        else:
            if v > 0:
                num_colors += 1

    if num_colors == 0:
        if colors["wild"] > 0:
            print("{} {}".format(1, colors["wild"], 8))
        else:
            print("0 0")
    else:
        print("{} {}".format(num_colors, num_colors + colors["wild"]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
