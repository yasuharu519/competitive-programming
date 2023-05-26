class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        m = len(grid[0])

        answer = [0] * m

        for col in range(m):
            maxLength = 0
            for row in range(n):
                maxLength = max(maxLength, len(str(grid[row][col])))
            answer[col] = maxLength
        
        return answer

        