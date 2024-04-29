#!/usr/bin/env python3


def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    stack = []
    for a in A:

        last_a = a
        while stack and stack[-1] == last_a:
            p = stack.pop()
            last_a = p + 1
        stack.append(last_a)
    print(len(stack))
    return

if __name__ == '__main__':
    main()
