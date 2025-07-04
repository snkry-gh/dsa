class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        vis = [[False for i in range(c)] for j in range(r)]

        q = []
        
        for i in range(r):
            
            if grid[i][0] == 1:
                q.append((i,0))
                vis[i][0] = True

            if grid[i][c - 1] == 1:
                q.append((i, c - 1))
                vis[i][c - 1] = True

        for j in range(c):
            if grid[0][j] == 1:
                q.append((0, j))
                vis[0][j] = True
            
            if grid[r - 1][j] == 1:
                q.append((r - 1, j))
                vis[r - 1][j] = True

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            _r, _c = q.pop(0)

            for dr, dc in dir:
                nr, nc = _r + dr, _c + dc
                
                if 0 <= nr < r and 0 <= nc < c and not vis[nr][nc]:
                    if grid[nr][nc] == 1:
                        q.append((nr, nc))
                        vis[nr][nc] = True

        count = 0

        for i in range(r):
            for j in range(c):
                if not vis[i][j] and grid[i][j] == 1:
                    count += 1
        
        return count