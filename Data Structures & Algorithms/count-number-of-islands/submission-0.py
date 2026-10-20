from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for i in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(r, c):
            vis[r][c] = 1
            Q = deque()
            Q.append((r, c))
            while Q:
                r, c = Q.popleft()
                for delRow,delCol in directions:
                        nRW = r + delRow
                        nCL = c + delCol
                        if (
                            nRW >= 0
                            and nRW < n
                            and nCL >= 0
                            and nCL < m
                            and grid[nRW][nCL] == "1"
                            and not vis[nRW][nCL]
                        ):
                            vis[nRW][nCL] = 1
                            Q.append((nRW, nCL))

        count = 0
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col] == "1":
                    count += 1
                    bfs(row, col)

        return count
