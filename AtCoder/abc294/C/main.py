import sys
from string import ascii_uppercase


def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    As = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    Bs = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    As = [(x, "A{}".format(i)) for i, x in enumerate(As)]
    Bs = [(x, "B{}".format(i)) for i, x in enumerate(Bs)]

    merged = sorted(As + Bs)

    result = [(v[1], i+1) for i, v in enumerate(merged)]

#     print([x for x in filter(lambda x: x[0].startswith("A"), result)])
#     print([x for x in filter(lambda x: x[0].startswith("B"), result)])
    print(
        " ".join([str(x[1]) for x in sorted(filter(lambda x: x[0].startswith("A"), result), key=lambda x: x[1])]))
    print(
        " ".join([str(x[1]) for x in sorted(filter(lambda x: x[0].startswith("B"), result), key=lambda x: x[1])]))


if __name__ == "__main__":
    main()
