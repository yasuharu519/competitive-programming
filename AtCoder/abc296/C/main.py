import sys


def main():
    N, X = [int(x) for x in sys.stdin.readline().strip().split()]
    nums = [int(x) for x in sys.stdin.readline().strip().split()]
    nums.sort(reverse=True)
    passed = set()
    for i in nums:
        passed.add(i)
        if (i+X) in passed:
            print("Yes")
            sys.exit(0)
    for i in nums:
        passed.add(i)
        if (i+X) in passed:
            print("Yes")
            sys.exit(0)
    print("No")


if __name__ == "__main__":
    main()
