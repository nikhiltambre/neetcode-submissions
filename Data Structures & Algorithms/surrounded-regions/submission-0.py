class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        queue = deque()
        # mark edges connected as visited
        for r in range(n):
            for c in range(m):
                if (r == 0 or r == n - 1 or c == 0 or c == m - 1) and board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "U"

        # mark every node connected to edge as visited
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O":
                    board[nr][nc] = "U"
                    queue.append((nr, nc))
        # mark X to remaining elements
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "U":
                    board[r][c] = "O"
