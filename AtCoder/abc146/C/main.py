#!/usr/bin/env python3
def main():
    A, B, X = list(map(int, input().strip().split()))

    ok, ng = 0, pow(10, 9) + 1
    while ok + 1 < ng:
        mid = (ok + ng) // 2
        num = A * mid + len(str(mid)) * B
        if num <= X:
            ok = mid
        else:
            ng = mid
    print(ok)
    return


if __name__ == '__main__':
    main()
