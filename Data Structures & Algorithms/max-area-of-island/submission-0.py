from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        RW, CL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vis = [[0] * CL for i in range(RW)]

        def bfs(r, c):
            vis[r][c] = 1
            cnt = 0
            Q = deque()
            Q.append((r, c))
            while Q:
                row, col = Q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < RW and 0 <= nc < CL and grid[nr][nc] == 1 and not vis[nr][nc]:
                        Q.append((nr, nc))
                        vis[nr][nc] = 1
                cnt += 1
            return cnt

        result = 0
        for r in range(RW):
            for c in range(CL):
                if not vis[r][c] and grid[r][c] == 1:
                    result = max(result, bfs(r, c))
        return result
