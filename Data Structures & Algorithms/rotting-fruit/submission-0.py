from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        Q = deque()
        freshCount = 0
        # counting fresh and queueing rotten
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    Q.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1
        cnt = 0
        while Q and freshCount>0:
            for _ in range(len(Q)):
                r, c = Q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # mark as rotton
                        Q.append((nr, nc))
                        freshCount -= 1
            cnt += 1

        return cnt if freshCount == 0 else -1
