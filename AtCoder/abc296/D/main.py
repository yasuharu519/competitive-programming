import sys
import math


def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    min_x = float("inf")

    for a in range(1, int(math.sqrt(M)) + 1):
        if M % a == 0:
            b = M // a

            if a <= N and b <= N:
                min_x = min(min_x, a * b)
    if min_x == float("inf"):
        print(-1)
    else:
        print(min_x)


if __name__ == "__main__":
    main()
