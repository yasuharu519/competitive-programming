from collections import deque


class Solution:

    def score(self, pins: List[int]) -> int:
        queue = deque()

        score = 0

        for pin in pins:
            if 10 in queue:
                score += pin * 2
            else:
                score += pin

            queue.append(pin)
            if len(queue) > 2:
                queue.popleft()

        return score

    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = self.score(player1)
        score2 = self.score(player2)

        if score1 == score2:
            return 0
        elif score1 > score2:
            return 1
        else:
            return 2
