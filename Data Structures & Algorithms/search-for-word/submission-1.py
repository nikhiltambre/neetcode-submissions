class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        RW, CL = len(board), len(board[0])
        path = set()
         
        def dfs(r, c, i):
            if i == len(word):
                return True

            if(r < 0 or c < 0 or r >= RW or c >= CL or word[i]!=board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            #4^len(word) TC
            found = (
                   dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))

            return found

        # rw*cw tc
        for r in range(RW):
            for c in range(CL):
                if dfs(r, c, 0):
                    return True
        return False

        #Total tc=O(rw*cw* 4^len(word))
        # Sc=len(word) for both path and recursion stack ==> O(len(word))