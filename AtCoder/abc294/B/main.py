import sys
from string import ascii_uppercase


def main():
    H, W = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    As = []
    for _ in range(H):
        As.append([ascii_uppercase[int(x)-1] if int(x) !=
                   0 else "." for x in sys.stdin.readline().strip().split(" ")])

    for row in As:
        print("".join(row))


if __name__ == "__main__":
    main()
