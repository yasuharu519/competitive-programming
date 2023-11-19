#!/usr/bin/env python3
import sys
from collections import deque

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, S: str, T: str):
    queue = deque()
    stamped = set()

    for i in range(N-M+1):
        if S[i:i+M] == T:
            queue.append(i)
    
    slist = list(S)
    
    while queue:
        stamp_index = queue.popleft()
        slist[stamp_index:stamp_index+M] = list("#" * M)
        stamped.add(stamp_index)

        for i in range(-M+1, M):
            if i == 0:
                continue
            index = stamp_index + i
            if index in stamped:
                continue
            if index < 0 or index >= N - M + 1:
                continue 
            flag = True
            for j in range(M):
                if slist[index+j] != T[j] and slist[index+j] != "#":
                    flag = False
            if flag:
                queue.append(index)
    print(YES if all([x == "#" for x in slist]) else NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(N, M, S, T)

if __name__ == '__main__':
    main()