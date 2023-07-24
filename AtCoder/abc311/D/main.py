#!/usr/bin/env python3
import sys
from collections import deque


def solve(N: int, M: int, S: "List[str]"):
    targetMap = [list(x) for x in S]
    S = targetMap
    start = (1, 1)
    queue = deque()
    queue.append(start)

    result = 0

    while queue:
        current_pos = queue.popleft()
        x, y = current_pos
        if S[x][y] != "x":
            S[x][y] = "x"
            result += 1

        # for +x
        next_x = x + 1
        last_x = x
        while S[next_x][y] != "#":
            if S[next_x][y] == ".":
                S[next_x][y] = "o"
                result += 1
            last_x = next_x
            next_x += 1
        if last_x != x and S[last_x][y] != "x":
            S[last_x][y] = "x"
            queue.append((last_x, y))

        # for -x
        next_x = x - 1
        last_x = x
        while S[next_x][y] != "#":
            if S[next_x][y] == ".":
                S[next_x][y] = "o"
                result += 1
            last_x = next_x
            next_x -= 1
        if last_x != x and S[last_x][y] != "x":
            S[last_x][y] = "x"
            queue.append((last_x, y))

        # for +y
        next_y = y + 1
        last_y = y
        while S[x][next_y] != "#":
            if S[x][next_y] == ".":
                S[x][next_y] = "o"
                result += 1
            last_y = next_y
            next_y += 1
        if last_y != y and S[x][last_y] != "x":
            S[x][last_y] = "x"
            queue.append((x, last_y))

        # for -y
        next_y = y - 1
        last_y = y
        while S[x][next_y] != "#":
            if S[x][next_y] == ".":
                S[x][next_y] = "o"
                result += 1
            last_y = next_y
            next_y -= 1
        if last_y != y and S[x][last_y] != "x":
            S[x][last_y] = "x"
            queue.append((x, last_y))
    
    print(result)
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
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, M, S)

if __name__ == '__main__':
    main()
