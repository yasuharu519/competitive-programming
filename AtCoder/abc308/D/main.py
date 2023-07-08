#!/usr/bin/env python3
import sys
import heapq

MOD = 5  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, S: "List[str]"):
    if S[0][0] != "s":
        print(NO)
        return

    queue = []
    queue.append((H-1 + W-1, 0, 0, 0, set()))

    snuke = "snuke"
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        _, x, y, c, path = heapq.heappop(queue)
        path.add((x, y))

        if x == H-1 and y == W-1:
            print(YES)
            return

        for dir in directions:
            nextX, nextY, nextC = x + dir[0], y + dir[1], (c + 1) % MOD
            rest = (H-1-nextX) + (W-1-nextY)
            if 0 <= nextX <= H - 1 and 0 <= nextY <= W - 1 and (nextX, nextY) not in path and S[nextX][nextY] == snuke[nextC]:
                queue.append((rest, nextX, nextY, nextC, path))
    
    print(NO)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
