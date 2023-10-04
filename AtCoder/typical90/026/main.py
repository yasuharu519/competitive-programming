#!/usr/bin/env python3
import sys
from collections import defaultdict, deque


def solve(N: int, A: "List[int]", B: "List[int]"):
    adj = defaultdict(list)

    for a, b in zip(A, B):
        adj[a].append(b)
        adj[b].append(a)

    redset = set()
    greenset = set()

    def traverse(i: int, isRed: bool):
        queue = deque()
        queue.append((i, isRed, -1))

        while queue:
            node, colorRed, prev = queue.popleft()
            if colorRed:
                redset.add(node)
            else:
                greenset.add(node)

            for next_node in adj[node]:
                if next_node == prev:
                    continue
                if next_node in redset or next_node in greenset:
                    continue
                queue.append((next_node, not colorRed, node))

    for i in range(1, N + 1):
        if i in redset or i in greenset:
            continue

        traverse(i, True)

    if len(redset) > len(greenset):
        l = list(redset)[:N // 2]
        print(" ".join(map(str, l)))
    else:
        l = list(greenset)[:N // 2]
        print(" ".join(map(str, l)))

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == '__main__':
    main()
