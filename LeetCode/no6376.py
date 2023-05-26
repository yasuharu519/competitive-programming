class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        maxRowCount = 0
        maxRowIndex = 0

        for i, row in enumerate(mat):
            countOne = sum([1 for x in row if x == 1])
            if countOne > maxRowCount:
                maxRowCount = countOne
                maxRowIndex = i

        return [maxRowIndex, maxRowCount]
