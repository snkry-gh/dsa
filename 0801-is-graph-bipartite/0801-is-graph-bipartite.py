class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color = [-1] * n

        def dfs(node, c):
            color[node] = c

            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if not dfs(neighbour, 1-c): return False
                elif color[neighbour] == color[node]:
                    return False
            
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0): return False

        return True