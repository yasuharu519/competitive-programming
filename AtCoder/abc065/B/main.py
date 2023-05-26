import sys


def main():
    N = int(sys.stdin.readline().strip())
    buttons = []
    for i in range(N):
        buttons.append(int(sys.stdin.readline().strip()))

    current = 1
    passed = set()

    while current not in passed:
        if current == 2:
            print(len(passed))
            return
        passed.add(current)
        current = buttons[current-1]

    print(-1)


if __name__ == "__main__":
    main()
