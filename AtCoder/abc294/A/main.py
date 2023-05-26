import sys


def main():
    N = int(sys.stdin.readline().strip())
    As = sys.stdin.readline().strip().split(" ")

    print(" ".join([x for x in As if int(x) % 2 == 0]))


if __name__ == "__main__":
    main()
