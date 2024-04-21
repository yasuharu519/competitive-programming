#!/usr/bin/env python3

def main():
    S = input().strip()
    if S[:3] != "ABC":
        print("No")
    num = S[3:]
    for i in range(1, 350):
        if i == 316:
            continue
        if num == "{:03}".format(i):
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()
