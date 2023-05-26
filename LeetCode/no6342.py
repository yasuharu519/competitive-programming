from collections import defaultdict


class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        rowIndex = {}
        colIndex = {}

        rowCounter = defaultdict(int)
        colCounter = defaultdict(int)

        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                rowIndex[val] = i
                colIndex[val] = j

        for i, v in enumerate(arr):
            row, col = rowIndex[v], colIndex[v]

            rowCounter[row] += 1
            colCounter[col] += 1

            if rowCounter[row] == n or colCounter[col] == m:
                return i

        return -1
