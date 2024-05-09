#!/usr/bin/env python3

def main():
    stack = []
    while True:
        A = input().strip()
        stack.append(A)
        if A == "0":
            break
    
    while stack:
        print(stack.pop())


if __name__ == '__main__':
    main()
