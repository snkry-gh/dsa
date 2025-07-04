class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        r = len(mat)
        c = len(mat[0])

        vis = [[False for i in range(c)] for j in range(r)]
        res = [[0 for i in range(c)] for j in range(r)]

        q = []

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[i][j] = True
        
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            _r, _c, dis = q.pop(0)

            res[_r][_c] = dis

            for dr, dc in dir:

                nr, nc = _r + dr, _c + dc

                if 0 <= nr < r and 0 <= nc < c and not vis[nr][nc]:
                    q.append((nr, nc, dis + 1))
                    vis[nr][nc] = True
        
        return res