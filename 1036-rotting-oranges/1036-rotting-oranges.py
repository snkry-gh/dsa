class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if n == 0:
            return -1

        m = len(grid[0])

        fresh = 0
        rotten = []
        minutes = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while rotten and fresh > 0:
            minutes += 1

            for _ in range(len(rotten)):
                x, y = rotten.pop(0)

                for dx, dy in directions:
                    _x, _y = x + dx, y + dy

                    if _x < 0 or _x == n or _y < 0 or _y == m:
                        continue
                    
                    if grid[_x][_y] == 0 or grid[_x][_y] == 2:
                        continue
                    
                    fresh -= 1
                    grid[_x][_y] = 2

                    rotten.append((_x, _y))
        
        return minutes if fresh == 0 else -1
