class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, n):
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j, n)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i, n)

        return provinces