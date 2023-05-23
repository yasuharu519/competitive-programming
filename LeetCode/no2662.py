import heapq
from typing import List
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads = [[a, b, c, d, e] for a, b, c, d, e in specialRoads if (abs(a-c) + abs(b-d)) > e]

        dp = {tuple(start): 0}
        queue = [(0, tuple(start))]
        
        while queue:
            currentCost, currentPos = heapq.heappop(queue)

            for x1, y1, x2, y2, c in specialRoads:
                tmp = currentCost + (abs(currentPos[0] - x1) + abs(currentPos[1] - y1)) + c
                if (x2, y2) not in dp or tmp < dp[(x2, y2)]:
                    dp[(x2, y2)] = tmp
                    heapq.heappush(queue, (tmp, (x2, y2)))
        
        result = float('inf')
        for (p, q), cost in dp.items():
            tmp = cost + (abs(target[0]-p) + abs(target[1]-q))
            result = min(result, tmp)
        return result

if __name__ == "__main__":
    s = Solution()
    start = [1,1]
    target = [4,5]
    specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]

    print(s.minimumCost(start, target, specialRoads))