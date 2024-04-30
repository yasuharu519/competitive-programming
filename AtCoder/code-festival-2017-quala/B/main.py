#!/usr/bin/env python3
YES = "Yes"  # type: str
NO = "No"  # type: str

def main():
    N, M, K = list(map(int, input().strip().split()))

    for i in range(N+1):
        for j in range(M+1):
            tmp = i * (M-j) + (N-i) * j
            if tmp == K:
                print(YES)
                return
    print(NO)
    return

if __name__ == '__main__':
    main()
