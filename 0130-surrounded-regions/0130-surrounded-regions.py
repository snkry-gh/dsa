class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        r = len(board)
        c = len(board[0])

        vis = [[False for i in range(c)] for j in range(r)]

        q = []

        for i in range(r):
            if board[i][0] == "O":
                q.append((i, 0))
                vis[i][0] = True
            
            if board[i][c - 1] == "O":
                q.append((i, c - 1))
                vis[i][c - 1] = True

        for j in range(c):
            if board[0][j] == "O":
                q.append((0, j))
                vis[0][j] = True
            
            if board[r - 1][j] == "O":
                q.append((r - 1, j))
                vis[r - 1][j] = True

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            _r, _c = q.pop(0)

            for dr, dc in dir:
                nr, nc = _r + dr, _c + dc
                
                if 0 <= nr < r and 0 <= nc < c and not vis[nr][nc]:
                    if board[nr][nc] == "O":
                        q.append((nr, nc))
                        vis[nr][nc] = True

        for i in range(r):
            for j in range(c):
                if not vis[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
        
        return board