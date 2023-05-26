import sys
from collections import deque
import heapq


def main():
    N, Q = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    events = []
    for _ in range(Q):
        events.append(sys.stdin.readline().strip())

    Nlist = [x+1 for x in range(N)]

    notcalled = deque(Nlist)
    called = []

    for event in events:
        eventType = event[0]
        if eventType == "1":
            number = notcalled.popleft()
            heapq.heappush(called, number)
        elif eventType == "2":
            number = int(event.split(" ")[1])
            called = [x for x in called if x != number]
            heapq.heapify(called)
        elif eventType == "3":
            print(called[0])


if __name__ == "__main__":
    main()
