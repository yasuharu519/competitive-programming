import sys


def main():
    l = []
    for i in range(8):
        l.append(sys.stdin.readline().strip())

    chars = "abcdefgh"
    for i, m in enumerate(reversed(l)):
        for c, v in zip(chars, m):
            if v == "*":
                print("{}{}".format(c, i+1))
                break


if __name__ == "__main__":
    main()
