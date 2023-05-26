# coding:utf-8
import sys
from typing import List
from collections import defaultdict
import heapq
import bisect


def solve(N: int, Q: int, query: List[List[int]]):
    # list 構造の N 個のリスト
    boxes = [[] for _ in range(N)]
    #  数 i が書かれたカードが入っている箱の番号を保持する
    cardToBox = defaultdict(list)

    for q in query:
        if q[0] == 1:
            # カードを箱に入れる
            card = q[1]
            box = q[2] - 1
            bisect.insort(boxes[box], card)

            if box+1 not in cardToBox[card]:
                bisect.insort(cardToBox[card], box+1)
        elif q[0] == 2:
            box = q[1] - 1
            print(" ".join(map(str, boxes[box])))
        else:
            card = q[1]
            print(" ".join(map(str, cardToBox[card])))


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    Q = int(sys.stdin.readline().strip())
    query = [list(map(int, sys.stdin.readline().strip().split()))
             for _ in range(Q)]

    solve(N, Q, query)
