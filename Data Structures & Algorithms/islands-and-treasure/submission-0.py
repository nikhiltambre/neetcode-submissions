class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m=len(grid),len(grid[0])
        Q = deque()
        vis=[[0]*m for i in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(n):
            for col in range(m):
                if grid[row][col]==0:
                    Q.append((row,col,0))
                    vis[row][col]=1
        while Q:
         r,c,steps=Q.popleft()
         grid[r][c]=steps
         for dr,dc in directions: 
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<m and  not vis[nr][nc] and grid[nr][nc]==2147483647:
                Q.append((nr,nc,steps+1))
                vis[nr][nc]=1