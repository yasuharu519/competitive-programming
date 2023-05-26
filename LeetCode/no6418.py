from typing import List


class Solution:

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        currentColor = [0] * n
        answer = []
        count = 0

        for idx, col in queries:
            prev = currentColor[idx]
            if prev == col:
                answer.append(count)
            else:
                currentColor[idx] = col
                if n > 1:
                    if idx == 0:
                        if currentColor[idx + 1] == col:
                            count += 1
                        if prev != 0:
                            if currentColor[idx + 1] == prev and currentColor[
                                    idx + 1] != col:
                                count -= 1
                    elif idx == n - 1:
                        if currentColor[idx - 1] == col:
                            count += 1
                        if prev != 0:
                            if currentColor[idx - 1] == prev and currentColor[
                                    idx - 1] != col:
                                count -= 1
                    else:
                        if currentColor[idx - 1] == col:
                            count += 1
                        if currentColor[idx + 1] == col:
                            count += 1
                        if prev != 0:
                            if currentColor[idx - 1] == prev and currentColor[
                                    idx - 1] != col:
                                count -= 1
                            if currentColor[idx + 1] == prev and currentColor[
                                    idx + 1] != col:
                                count -= 1
                answer.append(count)
        return answer


if __name__ == "__main__":
    s = Solution()
    n = 18
    queries = [[9, 5], [14, 15], [8, 14], [0, 4], [10, 19], [13, 11], [11, 18],
               [8, 15], [17, 9], [10, 1], [17, 8], [9, 13], [2, 17], [0, 10],
               [10, 15], [10, 19], [1, 13], [7, 1], [2, 7], [13, 16], [2, 12],
               [1, 19], [0, 9], [4, 1], [1, 7], [3, 18], [10, 7], [13, 2],
               [13, 9], [0, 17], [14, 11], [12, 7], [12, 18], [16, 15],
               [16, 13], [7, 12], [15, 12], [7, 18], [15, 16], [15, 6]]
    print(s.colorTheArray(n, queries))
