import sys


def func(i: int) -> int:
    return i // 2 if i % 2 == 0 else 3 * i + 1


def solve(s: int):
    passed = set()

    current = s
    counter = 0
    while True:
        counter += 1
        if current in passed:
            print(counter)
            break
        passed.add(current)
        current = func(current)
    return


if __name__ == "__main__":
    s = int(sys.stdin.readline().strip())
    solve(s)
