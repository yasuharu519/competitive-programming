import heapq
from typing import List


class Solution:

    def calculate(self, from_, target):
        return abs(target[0] - from_[0]) + abs(target[1] - from_[1])

    def minimumCost(self, start: List[int], target: List[int],
                    specialRoads: List[List[int]]) -> int:

        specialRoadsIndex = {}

        minimamCost = float('inf')

        for x1, y1, x2, y2, cost in specialRoads:
            if not (x1, y1) in specialRoadsIndex:
                specialRoadsIndex[(x1, y1)] = {}
            specialRoadsIndex[(x1, y1)][(x2, y2)] = cost

        passed = {}
        queue = [(0, 0, start[0], start[1])]
        while queue:
            estimatedCost, currentCost, currentX, currentY = heapq.heappop(
                queue)

            if currentX == target[0] and currentY == target[1]:
                minimamCost = min(minimamCost, currentCost)
                continue
            if (currentX,
                    currentY) in passed and passed[(currentX,
                                                    currentY)] <= currentCost:
                continue
            passed[(currentX, currentY)] = currentCost

            for from_, value1 in specialRoadsIndex.items():
                for to_, cost in value1.items():
                    heapq.heappush(queue,
                                   (currentCost + self.calculate(
                                       (currentX, currentY), from_) + cost +
                                    self.calculate(to_, target),
                                    currentCost + self.calculate(
                                        (currentX, currentY), from_) + cost,
                                    to_[0], to_[1]))

            heapq.heappush(queue, (currentCost + self.calculate(
                (currentX, currentY), target), currentCost + self.calculate(
                    (currentX, currentY), target), target[0], target[1]))

        return minimamCost


if __name__ == "__main__":
    s = Solution()
    start = [1, 1]
    target = [10, 8]
    special = [[6, 4, 9, 7, 1], [5, 2, 2, 1, 3], [3, 2, 5, 5, 2]]
    print(s.minimumCost(start, target, special))