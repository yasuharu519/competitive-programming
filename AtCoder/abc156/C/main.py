import sys
import math


def main():
    N = int(sys.stdin.readline().strip())
    costs = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    m = max(costs)

    minCost = math.inf

    for i in range(m):
        s = sum([pow(x - (i+1), 2) for x in costs])
        minCost = min(minCost, s)

    print(minCost)


if __name__ == "__main__":
    main()
