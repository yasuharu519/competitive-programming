import sys


def main():
    A, B = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    counter = 0
    current = 1
    while current < B:
        current += (A-1)
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()
