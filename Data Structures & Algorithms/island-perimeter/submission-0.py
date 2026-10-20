class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    for delRow, delCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nRW = row + delRow
                        nCL = col + delCol
                        if nRW < 0 or nRW >= n or nCL < 0 or nCL >= m or grid[nRW][nCL] == 0:
                            perimeter += 1

        return perimeter
