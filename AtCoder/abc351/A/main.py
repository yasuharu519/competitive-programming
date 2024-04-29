#!/usr/bin/env python3

def main():
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    total_a = sum(A)
    total_b = sum(B)

    print(total_a-total_b+1)
    return

if __name__ == '__main__':
    main()
