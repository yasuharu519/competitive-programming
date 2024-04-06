#!/usr/bin/env python3
import sys


def solve(N: int, K: int, R: int, S: int, P: int, T: str):

    result = 0

    # 余りが mod になる index のものを見ていく
    for mod in range(K):

        ans = 0
        last_hand = ""

        # 各回は独立に自由な手を出せる
        for i in range(mod, N, K):
            c = T[i]
            
            if c == "r":
                if last_hand != "p":
                    ans += P
                    last_hand = "p"
                else:
                    last_hand = ""
            elif c == "s":
                if last_hand != "r":
                    last_hand = "r"
                    ans += R
                else:
                    last_hand = ""
            else:
                if last_hand != "s":
                    last_hand = "s"
                    ans += S
                else:
                    last_hand = ""
        
        result += ans
    
    print(result)
    return


def main():
    N, K = list(map(int, input().strip().split()))
    R, S, P = list(map(int, input().strip().split()))
    T = input().strip()
    solve(N, K, R, S, P, T)

if __name__ == '__main__':
    main()
