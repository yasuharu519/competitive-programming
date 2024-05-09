#!/usr/bin/env python3

def main():
    l = set()
    N = int(input().strip())
    for _ in range(N):
        i = input().strip()
        if i in l:
            continue
        if "".join([x for x in reversed(i)]) in l:
            continue
        l.add(i)
    print(len(l))

if __name__ == '__main__':
    main()
