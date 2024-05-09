#!/usr/bin/env python3
def main():
    N, L = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))

    print(len(list(filter(lambda x: x >= L, A))))

if __name__ == '__main__':
    main()
