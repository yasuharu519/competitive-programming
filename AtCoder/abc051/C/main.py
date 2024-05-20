#!/usr/bin/env python3
def main():
    sx, sy, tx, ty = list(map(int, input().strip().split()))

    dx, dy = tx-sx, ty-sy

    print("{}{}".format("U" * dy, "R" * dx), end="")
    print("{}{}".format("D" * dy, "L" * dx), end="")
    print("L{}{}D".format("U" * (dy + 1), "R" * (dx + 1)), end="")
    print("R{}{}U".format("D" * (dy + 1), "L" * (dx + 1)))



if __name__ == '__main__': 
    main()
